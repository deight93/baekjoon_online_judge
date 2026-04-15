import sys

sudoku = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]

row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))
        else:
            n = sudoku[i][j]
            row[i][n] = True
            col[j][n] = True
            box[(i//3)*3 + (j//3)][n] = True

def dfs(idx):
    if idx == len(zeros):
        for r in sudoku:
            print(*r, sep='')
        exit(0)

    y, x = zeros[idx]
    b = (y//3)*3 + (x//3)

    for n in range(1, 10):
        if not row[y][n] and not col[x][n] and not box[b][n]:
            sudoku[y][x] = n
            row[y][n] = col[x][n] = box[b][n] = True

            dfs(idx+1)

            sudoku[y][x] = 0
            row[y][n] = col[x][n] = box[b][n] = False

dfs(0)