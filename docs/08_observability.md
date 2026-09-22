# Observability

## What is Observability?

Observability is de ability to understand what is happening inside your systems at any given moment without having to guess.

## The 3 Pillars
 
### Metrics.
Numbers measured over time that describe the state of your systems.
- CPU usage, memory, request per second, error rate, latency.
- Collected by **Prometheus** every 15 seconds.

### Logs.
Record of events that happened in your application.
- INFO, WARN, ERROR, DEBUG.
- Indexed and searched with **Loki**.

### Traces.
The complete path of a request through your system.
- Shows exactly where time is spent 
- Collected with **Jaeger** or **OpenTelemetry**.

## Tools Used.

### Prometheus.
- Pull-based metrics collector.
- Scrapes / Metrics endpoint every 15 seconds.
- Story time-serires data.
- Query language: PromQL.

### Grafana 
- Visualization platform.
- Connects with Prometheus as data source.
- Create dashboards with real-time graphs.
- Configure Alerts.

## Helm Stack Installed.
``` BASH 
helm install monitoring prometheus-community/kube-prometheus-stack \
--namespace monitoring \
--create-namespace
```

**Includes: Prometheus + Grafana + AlertManager + Node Explorer**

## Key Concepts

### Service Monitor

Kubernetes objects that tells Prometheus which service to scrape:

``` yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata: 
  name: devops-webapp-monitor
  namespace: monitoring
  labels: 
    release: monitoring
spec: 
  selector: 
    matchLabels: 
      app: devops-webapp
  endpoints: 
  - port: htpp
    path: /metrics
    interval: 15s
```

### Prometheus Metrics in Python.

```python
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    'http_request_total',
    'Total HTTP request',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'request_latency',
    ['endpoint']
)
```

## PromQL Queries

- Request rate over 5 minutes
    ```bash
    rate(http_request_total[5m])
    ```
- Average latency
    ```bash 
    rate(http_request_durations_seconds_sum[5m])
    / rate(http_request_dutarions_seconds_count[5m])
    ```
- CPU usage by pod
    ```bash
    rate(container_cpu_usage_seconds_total[5m])
    ```

## Pull vs Push Model

- **Puhs** -> app send metrics to server (rysk can overload)
- **Pull** -> Prometheus goes to fetch metrics (controlled, scalable)

## Key Commands 
```BASH 
#Check monitoring pods
kubectl get pods -n monitoring

#Access Prometheus UI
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9091:9090 --address 0.0.0.0

#Access Grafana  
kubectl port-forward -n monitoring svc/monitoring-grafana 3000 --address 0.0.0.0

#Check ServiceMonitor 
kubectl get servicemonitor -n monitoring
```

