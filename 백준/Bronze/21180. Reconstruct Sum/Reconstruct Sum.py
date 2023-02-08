import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
a = deque([int(sys.stdin.readline().rstrip()) for _ in range(n)])
p = "BAD"
for _ in range(n):
    a2 = a.popleft()
    if a2 == sum(a):
        p = a2
        break
    else:
        a.append(a2)
print(p)