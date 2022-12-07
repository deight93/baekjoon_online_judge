import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

temp = {}
max_n = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if i+j in temp.keys():
            temp[i+j] += 1
        else:
            temp[i+j] = 1

        if temp[i+j] > max_n:
            max_n = temp[i+j]


for i in sorted(temp.items(), key=lambda x: x[1]):
    if i[1] == max_n:
        print(i[0])

