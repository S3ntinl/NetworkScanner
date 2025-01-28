#!/bin/bash


echo '               __                      __   _____                                 
   ____  ___  / /__      ______  _____/ /__/ ___/_________ _____  ____  ___  _____
  / __ \/ _ \/ __/ | /| / / __ \/ ___/ //_/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / / / /  __/ /_ | |/ |/ / /_/ / /  / , | ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/ /_/\___/\__/ |__/|__/\____/_/  /_/|_|/____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                                        By S3n                                                    
'


if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <ip_list_file>"
    exit 1
fi


if [ ! -f "$1" ]; then
    echo "[ + ] File '$1' does not exist."
    exit 1
fi

echo -e "[ + ] About to scan: \n"

while read -r ip; do
    if [ -n "$ip" ]; then 
        echo -e "[ + ] $ip \r"
    fi
done < "$1"

echo -e "\r"

while read -r ip; do
    if [ -n "$ip" ]; then 
        echo "[ + ] Scanning $ip..."
        nmap -p- -sCV --min-rate 5000 -T4 -n -Pn -oN "$ip" "$ip" 1>/dev/null
    fi
done < "$1"

echo "[ + ] Scanning complete."