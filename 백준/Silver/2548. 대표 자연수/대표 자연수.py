import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

c_list = []

i = 0
while True:
    i += 1
    c_list += [sum([abs(j-i) for j in n_list])]
    if len(c_list) > 3:
        if c_list[-3] <= c_list[-2] <= c_list[-1]:
            print(c_list.index(min(c_list))+1)
            break