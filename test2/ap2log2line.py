#!/usr/bin/python
#coding:utf-8

import sys
import re

for line in sys.stdin:
    if re.search(r'(Server has received)|(Server responded with)', line):
        content = line
        for readline in sys.stdin:
            if re.search(r'(^\s+$)|(201\d{1}-\d{2}-\d{2} )', readline): break
            content += ' ' + readline if re.search(r'\d+ [><] ', readline) else ' data => ' + readline
        print content.replace('\n','')
