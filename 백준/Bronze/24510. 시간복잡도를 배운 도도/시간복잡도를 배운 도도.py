import sys
import re

c = int(sys.stdin.readline().rstrip())

max_n = 0
for i in range(c):
    code = sys.stdin.readline().rstrip()
    if "for" in code or "while" in code:
        temp_max_n = len(re.findall("for", code))+len(re.findall("while", code))
        if temp_max_n > max_n:
            max_n = temp_max_n

print(max_n)
