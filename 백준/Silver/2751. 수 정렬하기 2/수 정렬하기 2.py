import sys

c = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(c)]
n_list.sort()

for i in n_list:
    print(i)