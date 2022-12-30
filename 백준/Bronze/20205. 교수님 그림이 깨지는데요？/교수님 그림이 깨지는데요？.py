import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
a = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(n)]

temp = []
for i in range(k*n):
    temp2 = []
    for j in a[i//k]:
        temp2 += ([str(j)]*k)
    temp.append(temp2)

for i in temp:
    print(" ".join(i))

