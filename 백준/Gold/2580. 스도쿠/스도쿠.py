import sys

input_s_list = [[int(j) for j in sys.stdin.readline().split(" ")] for i in range(9)]
z_list = []
for k1, i in enumerate(input_s_list):
    for k2, j in enumerate(i):
        if j == 0:
            z_list += [[k1, k2]]


def get_possibles(row, col):
    possibles = set(range(1, 10))
    possibles -= set(input_s_list[row])

    temp = set()
    for i in range(9):
        temp.add(input_s_list[i][col])
    possibles -= temp

    test = set()
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            test.add(input_s_list[i][j])
    possibles -= test
    return tuple(possibles)


def solve(i):
    if i == len(z_list):
        [print(*row) for row in input_s_list]
        sys.exit()
    row, column = z_list[i]
    possibles = get_possibles(row, column)
    for num in possibles:
        input_s_list[row][column] = num
        solve(i+1)
        input_s_list[row][column] = 0


solve(0)