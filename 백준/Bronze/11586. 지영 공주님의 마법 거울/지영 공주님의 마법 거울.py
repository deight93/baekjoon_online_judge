import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().rstrip() for i in range(n)]
k = int(sys.stdin.readline())

if k == 1:
    temp = [print(i) for i in input_list]
elif k == 2:
    for i in input_list:
        print(i[::-1])
elif k == 3:
    for i in input_list[::-1]:
        print(i)