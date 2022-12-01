import sys

n = int(sys.stdin.readline().rstrip())

xy = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

mx_x = max(xy, key=lambda x: x[2])[2]
mx_y = max(xy, key=lambda x: x[3])[3]
temp = [[0] * mx_x for _ in range(mx_y)]

for i in xy:
    for y in range(i[1], i[3]):
        for x in range(i[0], i[2]):
            temp[y][x] = 1

print(sum([sum(i) for i in temp]))
