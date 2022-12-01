import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in input_list:
    temp = []
    for j in i:
        temp += [j[::-1]]
    print(" ".join(temp))