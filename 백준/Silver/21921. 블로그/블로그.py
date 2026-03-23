import sys

n, x = map(int, sys.stdin.readline().split())
dau = list(map(int, sys.stdin.readline().split()))

c = sum(dau[:x])
m = c
cnt = 1

for i in range(x, n):
    c += dau[i]
    c -= dau[i-x]

    if c > m:
        m = c
        cnt = 1
    elif c == m:
        cnt += 1

if m == 0:
    print("SAD")
else:
    print(m)
    print(cnt)