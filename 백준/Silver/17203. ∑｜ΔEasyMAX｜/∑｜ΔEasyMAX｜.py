import sys

n, q = map(int, sys.stdin.readline().rstrip().split(" "))
a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for i in range(q):
    ql, qr = map(int, sys.stdin.readline().rstrip().split(" "))
    t = 0
    for j in range(ql-1, qr-1):
        t += abs(a[j]-a[j+1])
    print(t)

