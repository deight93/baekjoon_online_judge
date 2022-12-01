import sys

n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split(" "))

t = b + (a//2)
if t > n:
    print(n)
else:
    print(t)

