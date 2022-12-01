import sys

n = int(sys.stdin.readline())
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

temp = [input_list[0]]
for i in range(2, n+1):
    temp += [input_list[i-1]*i-sum(temp)]

[print(i, end=" ") for i in temp]