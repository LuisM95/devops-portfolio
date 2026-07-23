#! usr/bin/env python3
"""
DevOps Portfolio - Script #1
Author: Luis Martel
Description: Collects System information from a Linux Server.
             Useful for quick server diagnostics and auditing!

"""

import os
import platform
import subprocess

def get_system_info():
    """Display key system information."""
    print("=" * 45)
    print("   SYSTEM INFO - DevOps Portfolio")
    print("=" * 45)
    print(f"User:        {os.getenv('USER')}")
    print(f"OS:          {platform.system()} {platform.release()}")

    hostname = subprocess.run(['hostname'], capture_output=True, text=True)
    print(f"Hostname:    {hostname.stdout.strip()}")
    print(f"Directory:   {os.getcwd()}")

    disk = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    lines = disk.stdout.splitlines()
    print(f"Disk usage:  {lines[1].split()[4]} used")

    memory = subprocess.run(['free', '-h'], capture_output=True, text=True)
    mem_lines = memory.stdout.splitlines()
    print(f"Memory:      {mem_lines[1].split()[2]} used")

    print("=" * 45)


if __name__=='__main__':
    get_system_info()
