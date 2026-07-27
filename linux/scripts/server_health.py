#! /usr/bin/env python3
"""
DevOs Portafolio - Script #2
Author: Luis Martel
Description: Server Health Check Script. 
             Monitor, disk, memory and critical processes!
"""

import subprocess

def check_disk():
    """ Check disk usage and alert if above 80%."""
    print("\n [DISK_USAGE]")
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    for line in lines[1:]: #skip header error
        parts = line.split() 
        if len(parts) >= 5:
            usage = int(parts[4].replace('%', ''))
            status = "WARNING" if usage > 80 else "OK"
            print(f" {status} | {parts[5]} -> {parts[4]} used")


def check_memory():
    """Check Memory and swap usage"""
    print("\n [MEMORY_USAGE]")
    result = subprocess.run(['free', '-h'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    mem = lines[1].split()
    swap = lines[2].split()
    print(f"RAM -> Total: {mem[1]} | Used: {mem[2]} | Free: {mem[3]} ")
    print(f"SWAP -> Total: {swap[1]} | Used: {swap[2]} | Free: {swap[3]}")


def check_processes():
    """Check if critical processes are running"""
    print("\n [CRITICAL_PROCESSES]")
    processes = ['firewalld','sshd', 'systemd']
    for proc in processes:
        result = subprocess.run(
            ['pgrep', proc], capture_output=True, text=True
                )
        status = 'RUNNING' if result.returncode == 0 else 'NOT FOUND'
        print(f" {status} | {proc} ")


def main():
    print("=" * 45)
    print(" SERVER HEALTH CHECK - DevOps portfolio ")
    print("=" * 45)
    check_disk()
    print("=" * 45)
    check_memory()
    print("=" * 45)
    check_processes()
    print("=" *45)

if __name__=="__main__":
    main()
