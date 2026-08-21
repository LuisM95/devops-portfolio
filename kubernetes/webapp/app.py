#!/usr/bin/env python3

""" DevOps Portfolio - Kubernetes WebApp
Author: Luis Martel
Description: simple web server to deostrate kubernetes Deployments and services
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import json
import time
import os
import platform
import socket

# Define Metrics 

REQUEST_COUNT = Counter(
        'http_request_total',
        'Total HTTP request',
        ['method', 'endpoint', 'status']
        )
REQUEST_LATENCY = Histogram (
        'http_request_duration_seconds',
        'HTTP request latency',
        ['endpoint']
        )

class DevOpsHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def do_GET(self):
        start_time = time.time()

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {
                    'status' : 'ok',
                    'message' : 'DevOps Portfolio - Kubernetes App',
                    'pod' : socket.gethostname(),
                    'os' : platform.system(),
                    'version' : '1.0'
                    }
            self.wfile.write(json.dumps(response).encode())
            REQUEST_COUNT.labels('GET','/','200').inc()

        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {'status': 'healthy'}
            self.wfile.write(json.dumps(response).encode())
            REQUEST_COUNT.labels('GET', '/health', '200').inc() 

        elif self.path == '/metrics':
            output = generate_latest()
            self.send_response(200)
            self.send_header('Content-Type', CONTENT_TYPE_LATEST)
            self.send_header('Content-Length', str(len(output)))
            self.end_headers()
            self.wfile.write(output)
            return
            

        else:
            self.send_response(404)
            self.end_headers()
            REQUEST_COUNT.labels('GET', self.path, '404').inc()

        duration = time.time() - start_time
        REQUEST_LATENCY.labels(self.path).observe(duration)

    def log_message(self, format, *args):
        print(f'[{self.address_string()}] {format % args}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8080))
    server = HTTPServer(('0.0.0.0',port), DevOpsHandler)
    print(f'Server Running on port: {port}')
    server.serve_forever()
