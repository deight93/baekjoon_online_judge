import sys
sys.setrecursionlimit(10**6)

dy = (-1, -1, -1, 1, 1, 1, 0, 0)
dx = (-1, 0, 1, -1, 0, 1, -1, 1)

def dfs(y, x):
    m[y][x] = 0

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if m[ny][nx] == 1:
                dfs(ny, nx)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not (w and h):
        break

    m = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)