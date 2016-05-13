import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'\bcat\b',line)
    if len(result) != 0:
        print(line)
        #print(len(result))
        #print(result)