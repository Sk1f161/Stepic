import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    #result = re.findall(r'z\w{3}z',line)
    if re.findall(r'z\w{3}z',line):
        print(line)