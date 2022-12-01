
import sys

n = sys.stdin.readline().rstrip()
temp = "A"
s = 0
for i in n:
    if ord(i)-ord(temp) <= 0:
        s += min(abs(ord(i) - ord(temp)), abs(26 + (ord(i) - ord(temp))))
    else:
        s += min(abs(ord(i) - ord(temp)), abs(26 - (ord(i) - ord(temp))))
    temp = i
print(s)
