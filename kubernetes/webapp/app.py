#!/usr/bin/env python3

""" DevOps Portfolio - Kubernetes WebApp
Author: Luis Martel
Description: simple web server to deostrate kubernetes Deployments and services
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import platform
import socket

class DevOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
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

        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = { 'status' : 'healthy' }
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f'[{self.address_string()}] {format % args}')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8080))
    server = HTTPServer(('0.0.0.0',port), DevOpsHandler)
    print(f'Server Running on port: {port}')
    server.serve_forever()
