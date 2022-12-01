import sys

input_list = [sys.stdin.readline().rstrip() for i in range(2)]

temp = [[0 for _ in range(len(input_list[1])+1)] for _ in range(len(input_list[0])+1)]

for i in range(1, len(input_list[0])+1):
    for j in range(1, len(input_list[1])+1):
        if input_list[0][i-1] == input_list[1][j-1]:
            temp[i][j] = temp[i-1][j-1] + 1
        else:
            temp[i][j] = max(temp[i-1][j],  temp[i][j-1])

print(max([max(i) for i in temp]))