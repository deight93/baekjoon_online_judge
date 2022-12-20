import sys

n = int(sys.stdin.readline().rstrip())
m = 0
for _ in range(n):
    a, d, g = map(int, sys.stdin.readline().rstrip().split(" "))

    if a == d + g:
        if (a*(d+g))*2 > m:
            m = (a*(d+g))*2
    else:
        if a * (d + g) > m:
            m = a*(d+g)
print(m)
