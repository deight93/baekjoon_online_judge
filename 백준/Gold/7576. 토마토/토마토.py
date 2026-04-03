import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

temp = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            temp.append([j, i])

q = deque(temp)
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0:
            arr[ny][nx] = arr[y][x] + 1
            q.append([nx, ny])


max_num = max(arr[i][j] for i in range(n) for j in range(m))-1
ck_zero = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ck_zero = True
if ck_zero:
    max_num = -1

if max_num == 1:
    max_num = 0

print(max_num)
