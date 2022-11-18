import sys

n = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            input_list[i][j] = max([input_list[i][j] + input_list[i-1][j]])
        elif j == i:
            input_list[i][j] = max([input_list[i][j] + input_list[i - 1][j - 1]])
        else:
            input_list[i][j] = max([input_list[i][j] + input_list[i-1][j], input_list[i][j] + input_list[i-1][j-1]])

print(max(input_list[n-1]))