import sys
import os
import subprocess

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 networkScanner.py <ip_list>")
        sys.exit(1)

    
    ip_list = sys.argv[1]

    
    if not os.path.isfile(ip_list):
        print(f"[ + ] File '{ip_list}' does not exist.")
        sys.exit(1)

    print("[ + ] About to scan:\n")

    
    with open(ip_list, 'r') as file:
        ip_list = [line.strip() for line in file if line.strip()]  
        for ip in ip_list:
            print(f"[ + ] {ip}")

    print("\n")

    
    for ip in ip_list:
        print(f"[ + ] Scanning {ip}...")
        try:
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
                    f"{ip}_scan.txt",
                    ip,
                ],
                stdout=subprocess.DEVNULL,  
                stderr=subprocess.DEVNULL,
            )
        except Exception as e:
            print(f"[ - ] Error scanning {ip}: {e}")

    print("[ + ] Scanning complete.")

if __name__ == "__main__":
    main()
