import sys

n = int(sys.stdin.readline().rstrip())

t = 0
for i in range(n):
    p = sys.stdin.readline().rstrip()
    t += (int(p[:-1])**int(p[-1]))

print(t)

