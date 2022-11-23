import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
v = [0 for i in range(100001)]

q = deque([n])
while q:
    n = q.popleft()
    if n == k:
        print(v[n])
        break
    for i in [n-1, n+1, 2*n]:
        if 0 <= i <= 100000 and not v[i]:
            v[i] = v[n] + 1
            q.append(i)
