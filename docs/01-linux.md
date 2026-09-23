# Linux & Systems Fundamentals

## What is Linux?
Linux is the operating system that powers most servers in production.
As a DevOps engineer, the terminal is your home.

## Key Commands

### System Information
```bash
whoami          # current user
uname -a        # kernel and architecture
hostnamectl     # hostname details
uptime          # server uptime and load average
```

### Disk & Memory
```bash
df -h           # disk usage
free -h         # RAM and swap usage
du -sh ~        # home directory size
```

### Processes
```bash
top             # real-time processes
ps aux          # list all processes
ps aux | grep python  # filter by name
kill <PID>      # terminate process
```

### Files & Permissions
```bash
ls -la          # list with permissions
chmod 755 file  # set permissions
chown user file # change owner
find / -name "*.py"  # search files
grep -r "ERROR" /var/log/  # search in files
```

### Services (systemd)
```bash
systemctl start sshd    # start service
systemctl stop sshd     # stop service
systemctl restart sshd  # restart service
systemctl status sshd   # check status
systemctl enable sshd   # start on boot
systemctl disable sshd  # don't start on boot
systemctl is-enabled sshd  # check if enabled
```

### Networking
```bash
ip addr show        # show IPs
ip route show       # show routes
ss -tuln            # open ports
ping google.com     # test connectivity
nslookup google.com # DNS resolution
curl -I https://google.com  # HTTP headers
```

### Logs
```bash
tail -n 20 /var/log/messages    # last 20 lines
tail -f /var/log/messages       # follow in real time
grep -i "error" /var/log/messages  # filter errors
```

## Python Scripts Created
| Script | Description |
|--------|-------------|
| `system_info.py` | Collects system information |
| `server_health.py` | Monitors disk, memory, processes and logins |
| `network_diagnostic.py` | Checks connectivity, DNS and HTTP status |

## Key Concepts
- **stdout vs stderr** — standard output vs error output
- **Pipes** — connect commands: `ps aux | grep python | wc -l`
- **Permissions** — 644 (files), 755 (scripts), 600 (private keys)
- **Processes** — every running program has a PID
- **Systemd** — init system that manages services in RHEL/Ubuntu
