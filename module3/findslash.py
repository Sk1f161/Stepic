import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'\\',line):
        print(line)
