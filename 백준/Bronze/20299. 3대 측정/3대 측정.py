import sys

n, k, l = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

temp = []
for i in input_list:
    if sum(i) >= k and i[0] >= l and i[1] >= l and i[2] >= l:
        temp += [i]

print(len(temp))
for i in temp:
    for j in i:
        print(j, end=" ")