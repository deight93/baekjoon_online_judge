import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < m and 0 <= ny < n):
                continue

            if visited[ny][nx] == -1 and arr[ny][nx] == '1':
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))

bfs(0, 0)
print(visited[n-1][m-1])