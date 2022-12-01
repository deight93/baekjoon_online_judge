
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

temp = [[0 for j in i] for i in input_list]

for i in range(n):
    for j in range(m):
        if i-1 == -1 and j-1 == -1:
            temp[i][j] = input_list[i][j]
        elif j-1 == -1:
            temp[i][j] = temp[i-1][j] + input_list[i][j]
            pass
        elif i-1 == -1:
            temp[i][j] = temp[i][j-1] + input_list[i][j]
        else:
            temp[i][j] = max([temp[i][j-1] + input_list[i][j], temp[i-1][j-1] + input_list[i][j],
                              temp[i-1][j] + input_list[i][j]])

print(temp[-1][-1])