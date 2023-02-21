import sys

n = int(sys.stdin.readline().rstrip())
r = 0
for _ in range(n):
    a, b = map(float, sys.stdin.readline().rstrip().split(" "))
    r += a*b
print("{:.3f}".format(r))

