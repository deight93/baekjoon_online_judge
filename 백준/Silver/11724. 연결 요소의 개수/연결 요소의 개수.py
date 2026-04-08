import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    for next_node in arr[node]:
        if not visited[next_node]:
            dfs(next_node)

cnt  = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)