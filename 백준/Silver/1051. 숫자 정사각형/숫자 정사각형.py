import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
min_nm = min(n, m)
a = [sys.stdin.readline().rstrip() for _ in range(n)]

max_s = 1
for i in range(n-1):
    for j in range(m-1):
        for k in range(1, min_nm):
            if k+i == n or k+j == m:
                break
            if len(set(list([a[i][j], a[i+k][j], a[i][j+k], a[i+k][j+k]]))) == 1:
                if max_s < (k+1)**2:
                    max_s = (k+1)**2
print(max_s)
