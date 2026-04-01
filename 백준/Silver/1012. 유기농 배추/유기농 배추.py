import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    cnt = 0

    def dfs(x, y):
        arr[y][x] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                dfs(j, i)

    print(cnt)
