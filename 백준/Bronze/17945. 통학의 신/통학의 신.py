import sys

A, B = map(int, sys.stdin.readline().rstrip().split(" "))

a = 1
b = 2*A
c = B

x1 = ((-1*b) + ((b**2)-4*a*c)**0.5)/2*a
x2 = ((-1*b) - ((b**2)-4*a*c)**0.5)/2*a
if x1 == x2:
    print(int(x1))
else:
    s_x = sorted([x1, x2])
    print(int(s_x[0]), int(s_x[1]))

