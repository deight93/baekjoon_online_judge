import sys

c = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for i in range(c)]
asc_list = sorted(n_list)

for i in asc_list:
    print(i)