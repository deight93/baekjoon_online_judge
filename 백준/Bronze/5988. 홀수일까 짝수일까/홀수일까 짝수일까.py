import sys

n = int(sys.stdin.readline())

input_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]

for i in input_list:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
