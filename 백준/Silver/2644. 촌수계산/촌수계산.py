import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [0] * (n+1)

def dfs(x, cnt):
    cnt += 1
    visited[x] += cnt
    for y in arr[x]:
        if not visited[y]:
            dfs(y, cnt)

cnt = 0
dfs(a, cnt)
print(visited[b]-1)