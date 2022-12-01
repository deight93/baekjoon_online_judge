import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = [i for i in range(1, 46)]
temp = []
for k, i in enumerate(n_list):
    for j in range(i):
        temp += [i]

print(sum(temp[a-1:b]))