import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()
        for next_node in arr[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    total = sum(visited)
    return total

min_total = float("INF")
ans = 0
for i in range(1, n+1):
    total = bfs(i)
    if min_total > total:
        min_total = total
        ans = i

print(ans)
