# Postmortem 001 - HTTP/1.0 Incompatibility with Kubernetes port-forward

## Date 
2026 - 08 - 24

## Author 
**Luis Martel** 

## Severity 
Medium - App was running but metrics endpoint unreachable through Kubernetes

## Summary 
The `/metrics` endpoint of `devops-webapp` was not returning data when access throgh Kubernetes port-forward, despite the app runnning correctly and the endpoint working locally without proxy.

## Timeline 
- App deployed to Kubernetes with a 3 replicas ✅
- `/metrics` enpoint added whit prometheus_client ✅
- Port-forward configured: `kubectl port-forward pod/.... 7777:8080` ✅
- `curl http://localhost:7777/metrics` returned empty response ❌
- First Observation by Luis: **"not that it could be a problem with the rollout that was made?"** - suspected the rollout didn't copy the app.py modifications correctly.
- Verified app.py inside container with `kubectl exec`: confirmed it HAD the new code ✅
- Verified port 8080 was open inside container using python socket. ✅
- Tested locally without port-forward: worked perfectly ✅
- Luis identified: **"isn't it that maybe some error in the docker image build?"** - suspected Docker Build issue. 
- Verified with `docker run -rm luismarteel/devops-webap:latest python3 -c "import prometheus_client; print('OK')` -> OK. ✅
- Used `curl -v` which revealed the key clue: `HTTP/1.0` and `no chunk, no close, no size`.
- Root cause identified: `HTTP/1.0` incompatibility with Kubernetes port-forward proxy.
- Fixed by adding `protocol_version = 'HTTP/1.1'` ✅

## What Luis Observed First.
Luis noticed that the rollout might not have applied the changes correctly because the container inside kubernetes had the old `app.py` without prometheus imports. After verifying with `kubectl exec -- cat /app/app.py`, it was confirmed the new code WAS there - ruling out the rollout theory.

Luis then suspected a docker build issue - that the image wasn't build with the new code. This was also ruled out by running prometheus_client import directly inside a container.

The real issue was only revealed when testing locally without port-forward proxy and comparing the behavior - pointing to the proxy layer as the problem.

## Root cause 
Python's `BaseHTTPServer` uses **HTTP/1.0** by default.

HTTP/1.0 does not require `Content-Length` headers and closes the connection after sending the response. Kubernetes port-forward acts as a proxy and expect HTTP/1.1 which requires `Content-Length` to know when the response ends. Without it, the proxy kept waiting for more data until timeout, resulting in an empty response.

```
curl -> port-forward(proxy) -> pod 
│
└── Expected HTTP/1.1 whit Content-Length 

Got HTTP/1.0 whitout Content-Length -> Proxy waited forever -> empty reponse
```

## Why it worked locally?
Whitout the port-forward proxy curl connected directly to the app. Curl and Python communicated directly whitout intermediary, so HTTP/1.0 worked fine whitout Content-Length.

## Diagnosti Process Used. 

- Layer1: **Network Connectivity ✅ (ping worked)**
- Layer2: **Port Open ✅ (Python socket confirmed port 8080 open)**
- Layer3: **Process Running ✅ (Python exec worked inside container)**
- Layer4: **Code Correct ✅ (Kubectl exec -- cat /app/app.py confirmed)**
- Layer5: **Docker Image Correct ✅ (prometheus_client import worked)**
- Layer6: **Proxy/Intermediary ❌ <- root cause found here.

## Solution.
Added `protocol_version = 'HTTP/1.1'` to the request handler class:

```python 
class DevOpsHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self)
    ...
```

Also added Content-Length header to all responses:

```python 
body = json.dumps(response).encode()
self.send_response(200)
self.send_header('Content-Type', 'application/json')
self.send_header('Content-Length', str(len(body)))
self.end_headers()
self.wfile.write(body)
```

## Key commands used for Diagnostic.

``` bash
# Verify app.py inside the container.
kubectl exec -it <pod> -- cat /app/app.py

# Test prometheus_client import
docker run -rm luismarteel/devops-webapp:latest python3 -c "import prometheus_client; print('OK')"

# Verify port open inside container
kubectl exec -it <pod> -- python3 -c "
import socket 
s = socket.socket()
s.connect(('localhost', 8080))
print('Port 8080 open')
"
# The commmand that revealed the root cause 
curl -v http://localhost:7777/metrics

# Output: HTTP/1.0 200 OK
# Output: not chunk, no close, no size. Assume close to signal end. 
```

## Lesson Learned.

### 1. Trust yours instincts but verify with data.
Luis suspected the rollout and the docker build - both valid hypotheses. The right approach is to verify each one systematically before moving on.

### 2. Always test through the proxy, not just directly.
Testing locally whitout port-forward is not enough. Always test the same way production will access the service.

### 3. Curl -v is your best friend.
The verbose flag revealed the key clue.

```bash 
HTTP/1.0 200 OK 
- no chunk, no close, no size. Assume close to signal end.
```

### 4. Silent failures are the hardest to bug.
The app Showed Running status, the port was open, the process was alive - everything looked fine. The failure was at the protocol level between layers.

## Prevention.
- Always add `protocol_version = 'HTTP/1.1'` when using BaseHTTPServer. ✅
- Always include `Content-Lenght` header in responses. ✅
- Test endpoints through port-forward before considering done. ✅
- Use `curl -v` for debbuging HTTP issues. ✅
- When something works locally but not in Kubernetes, suspect the proxy layer. ✅

