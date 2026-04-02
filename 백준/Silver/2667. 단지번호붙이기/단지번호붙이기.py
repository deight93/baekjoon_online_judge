import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline() for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if visited[ny][nx]:
            continue
        if arr[ny][nx] == '1':
            apt_complex[cnt] += 1
            dfs(nx, ny)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

apt_complex = {}
cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt += 1
            apt_complex[cnt] = 1
            dfs(j, i)

print(max(apt_complex.keys()))
for i in sorted(apt_complex.values()):
    print(i)