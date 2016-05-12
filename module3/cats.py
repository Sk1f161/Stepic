import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'cat+',line)
    if len(result) > 1:
        print(line)