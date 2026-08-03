#! /usr/bin/env python3
"""
DevOps Portfolio - Script #3 
Author: Luis Martel
Description: Network Diagnostic tool
             Checks Connectivity, DNS resolution and HTTP status
"""


import subprocess
import socket
import urllib.request
import urllib.error


def check_connectivity():
    """ Check Basic Connectivity """
    print("\n [CONECCTIVITY]")
    hosts = ["8.8.8.8", "1.1.1.1", "192.168.80.2"]
    for host in hosts: 
        result = subprocess.run(
                ["ping", "-c", "1", "-w", "2", host],
                capture_output=True, text=True
        )
        status = "OK" if result.returncode == 0 else "FAILED"
        print(f" {status} | ping {host} ")


def check_dns():
    """ Check DNS resolution for common domains. """
    print("\n [DNS RESOLUTION]")
    domains = ["google.com", "github.com", "cloudflare.com"]
    for domain in domains:
        try:
            ip = socket.gethostbyname(domain)
            print(f"  OK  |  {domain} -> {ip} ")
        except socket.gaierror: 
            print(f" FAILED  |  {domain}  -> Cloud not resolve ")


def check_http():
    """ Check Status HTTP of commond endopoints"""
    print("\n [HTTP STATUS]")
    urls = ["https://google.com", "https://github.com"]
    for url in urls:
        try:
            req = urllib.request.urlopen(url, timeout=5)
            print(f" {req.status} OK | {url}")
        except urllib.error.HTTPError as e:
            print(f" {e.code}  | {url}")
        except Exception as e:
            print(f" FAILED  | {url} -> {e}")


def get_network_info():
    """Display Network Local Information"""
    print("\n [NETWORK INFO]") 
    hostname = socket.gethostname()
    print(f" Hostname: {hostname}")
    result = subprocess.run(
            ['ip', 'addr', 'show', 'ens160'],
            capture_output=True, text=True
            )
    for line in result.stdout.splitlines():
        if 'inet' in line and 'inet6' not in line:
            local_ip = line.strip().split()[1]
            print(f' Local Ip: {local_ip}')


def main():
    print("=" * 45)
    print("Network Diagnostic")
    print("=" * 45)
    get_network_info()
    check_connectivity()
    check_dns()
    check_http()
    print("\n "+ "=" * 45)


if __name__=="__main__":
    main()


