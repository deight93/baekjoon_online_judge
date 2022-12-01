
import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

c = ""
for i in s[::n]:
    c += i
print(c)


