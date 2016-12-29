import sys
import re
import csv

index = {"ip":0,"day":1,"time":2,"act":3,"user":4,"uuid":5,"buy":6}

writer = csv.writer(sys.stdout)

for line in sys.stdin:
    row=["NA","NA","NA","NA","NA","NA","NA"]
    
    line = re.sub(r'"\s.*$', '', line)
    m = re.search(r'^([0-9.]+).*\[([^:]+):(\S+).*\?;(\S+)', line)

    row[index["ip"]] = m.group(1)
    row[index["day"]] = m.group(2)
    row[index["time"]] = m.group(3)

    for item in re.findall(r'(\w+)=([^;]+)', m.group(4)):
        key = item[0].strip()
        val = item[1].strip()
        if key in index:
            row[index[key]] = val

    writer.writerow(row)
