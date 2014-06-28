#!/bin/bash

IP=$1

wget  http://ip138.com/ips138.asp?ip=$IP -O /tmp/$IP.txt -o /dev/null
iconv -f GBK -t UTF-8 /tmp/$IP.txt | grep -A5 IP:$IP | sed -e 's/<[^<]*>//g'
rm -rf /tmp/$IP.txt
exit 0
