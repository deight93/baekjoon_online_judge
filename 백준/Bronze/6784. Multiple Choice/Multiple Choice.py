import sys

n = int(sys.stdin.readline().rstrip())
r = [sys.stdin.readline().rstrip() for i in range(n)]
a = [sys.stdin.readline().rstrip() for i in range(n)]

c = [1 for i, j in zip(r, a) if i == j]
print(sum(c))

