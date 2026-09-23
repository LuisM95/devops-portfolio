# Networking Documentation!

## Ip Address
The IP is a unique address of a server or computer connected within an Internet network

 ## DNS (Domain Name Service)
It's like a book phone that translates names into a IP addresses

## HTTP Protocol
It is an http transfer protocol without encryption, which uses port 80

## HTTPS Protocol
Http protocol with SSL/TLS encryption certificates, uses port 443

## Ports & Connections
```
Port 22: SSH
Port 80: HTTP
Port 443: HTTPS
Port 3000: Grafana
```

## Commands Network 
``` BASH
ip addr show     # Show all networks interfaces and their ips 
ip route show   # Show how traffic leave your server
ping             # Send ICMP packages to check if a host is alive and measure latency
nslookup         # Query DNS to resolve a domain to IP
curl -I          # Makes an HTTP request and displays only the response headers
ss -tuln         # Show all open ports on the server
traceroute       # Show the path the packages take to reach the destination, hop by hop
```

## HTTP Status
```
- 200  -> OK
- 301  -> Redirect
- 404  -> Not Found
- 500  -> Server Error
```
