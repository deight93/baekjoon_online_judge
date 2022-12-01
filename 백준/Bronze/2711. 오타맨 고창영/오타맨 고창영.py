import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().rstrip().split(" ") for i in range(n)]

for i in input_list:
    print(i[1][:int(i[0])-1]+i[1][int(i[0]):])