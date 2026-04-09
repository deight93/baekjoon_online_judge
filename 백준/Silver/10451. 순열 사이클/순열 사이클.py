import sys
from collections import deque
sys.setrecursionlimit(10**6)


def dfs(idx):
    if visited[idx]: return
    visited[idx] = True
    dfs(arr[idx])


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = deque(arr)
    arr.appendleft(0)

    visited = [False] * (n + 1)

    cnt = 0
    for i in range(1, n+1):
        if visited[i]: continue
        cnt += 1
        dfs(i)
    print(cnt)