import sys

n = int(sys.stdin.readline())
x_y_list = [[int(j) for j in input().split(" ")] for i in range(n)]
x_y_list.sort(key=lambda x: (x[1], x[0]))
for i in x_y_list:
    print(i[0], i[1])