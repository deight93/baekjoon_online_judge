import sys
import re

a = sys.stdin.readline().rstrip()

temp1 = [m for m in re.finditer('(?=(JOI))', a)]
temp2 = [m for m in re.finditer('(?=(IOI))', a)]

print(len(temp1))
print(len(temp2))