
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

temp_dict = {}
for _ in range(m):
    f_l = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    for i in f_l:
        if i in temp_dict.keys():
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

for i in range(1, n+1):
    if i in temp_dict.keys():
        print(temp_dict[i])
    else:
        print(0)