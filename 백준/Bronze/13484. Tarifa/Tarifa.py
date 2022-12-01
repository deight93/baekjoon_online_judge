
import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

t = x
for i in range(n):
    p = int(sys.stdin.readline().rstrip())
    t += (x-p)

print(t)
