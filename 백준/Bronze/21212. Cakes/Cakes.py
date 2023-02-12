import sys

n = int(sys.stdin.readline().rstrip())
p = 10001
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    p = min(p, b//a)
print(p)