import sys

x, y = map(float, sys.stdin.readline().rstrip().split(" "))
n = int(sys.stdin.readline().rstrip())

yx = y/x
xy = x/y
for _ in range(n):
    z, q = sys.stdin.readline().rstrip().split(" ")
    z = float(z)
    if q == "A":
        print(yx*z)
    else:
        print(xy*z)

