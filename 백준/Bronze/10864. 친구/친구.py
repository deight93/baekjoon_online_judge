import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]

temp = {}
for i in range(1, n+1):
    temp[i] = 0

for i in range(1, n+1):
    for j in input_list:
        if i in j:
            temp[i] += 1

[print(i) for i in temp.values()]
