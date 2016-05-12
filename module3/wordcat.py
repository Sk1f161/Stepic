import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'\bcat\W+',line)
    #if len(result) > 1:
    print(result)