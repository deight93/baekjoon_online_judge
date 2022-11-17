
import sys

n = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

for i in range(1, len(input_list)):
    input_list[i][0] = min(input_list[i - 1][1], input_list[i - 1][2]) + input_list[i][0]
    input_list[i][1] = min(input_list[i - 1][0], input_list[i - 1][2]) + input_list[i][1]
    input_list[i][2] = min(input_list[i - 1][0], input_list[i - 1][1]) + input_list[i][2]

print(min(input_list[n - 1][0], input_list[n - 1][1], input_list[n - 1][2]))
