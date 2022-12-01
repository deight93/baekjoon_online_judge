import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split(" "))

a = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
temp = [0] * n

ck = 0
for i in range(m):
    for j in range(n):
        temp[j] += a[j][i]
        if temp[j] >= k:
            print(j+1, i+1)
            ck = 1
            break
    if ck == 1:
        break


