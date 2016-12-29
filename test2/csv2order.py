import sys
import csv
import re

index = {"day":1,"user":4,"buy":6}

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

for row in reader:
    out = ["NA","NA","NA","NA","NA"]
    out[0] = row[index["day"]]
    out[1] = row[index["user"]]

    for item in re.findall(r'([0-9]+),([0-9]+),([0-9]+)', row[index["buy"]]):
        out[2] = item[0]
        out[3] = item[1]
        out[4] = item[2]
        writer.writerow(out)
