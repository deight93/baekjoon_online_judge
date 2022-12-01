import sys

k, n = map(int, sys.stdin.readline().rstrip().split(" "))
if n == 1:
    print(-1)
else:
    a = (k*n) // (-1*(1-n))
    if (k*n) % (-1*(1-n)):
        a += 1
    print(a)
