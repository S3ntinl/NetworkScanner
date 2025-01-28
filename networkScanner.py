#!/usr/bin/env python3

import sys
import os
import subprocess
from halo import Halo

ascii_art = r"""
▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖ ▗▄▖ ▗▄▄▖ ▗▖ ▗▖ ▗▄▄▖ ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▄▄▖ 
▐▛▚▖▐▌▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘▐▌   ▐▌   ▐▌ ▐▌▐▛▚▖▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌
▐▌ ▝▜▌▐▛▀▀▘  █  ▐▌ ▐▌▐▌ ▐▌▐▛▀▚▖▐▛▚▖  ▝▀▚▖▐▌   ▐▛▀▜▌▐▌ ▝▜▌▐▌ ▝▜▌▐▛▀▀▘▐▛▀▚▖
▐▌  ▐▌▐▙▄▄▖  █  ▐▙█▟▌▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▗▄▄▞▘▝▚▄▄▖▐▌ ▐▌▐▌  ▐▌▐▌  ▐▌▐▙▄▄▖▐▌ ▐▌
                                                                By S3n
"""

print(ascii_art)

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 networkScanner.py <ip_list>")
        sys.exit(1)

    
    ip_list = sys.argv[1]

    
    if not os.path.isfile(ip_list):
        print(f"[ + ] File '{ip_list}' does not exist.")
        sys.exit(1)

    print("IP List: \n")
    
    with open(ip_list, 'r') as file:
        ip_list = [line.strip() for line in file if line.strip()]  
        for ip in ip_list:
            print(f":: {ip}")

    print("\r")
    
    for ip in ip_list:
        try:
            spinner = Halo(text=f'Scanning {ip}...', spinner='dots')
            spinner.start()
            subprocess.run(
                [
                    "nmap",
                    "-p-",
                    "-sCV",
                    "--min-rate",
                    "5000",
                    "-T4",
                    "-n",
                    "-Pn",
                    "-oN",
                    ip,
                    ip,
                ],
                stdout=subprocess.DEVNULL,  
                stderr=subprocess.DEVNULL,
            )
            spinner.stop()
        except Exception as e:
            print(f"[ - ] Error scanning {ip}: {e}")

    print("[ + ] Scanning complete.")

if __name__ == "__main__":
    main()
