import sys

a, b = map(int, sys.stdin.readline().strip().split(" "))

x = (a+b)/2
y = a-x

if x.is_integer() and y.is_integer() and x >= 0 and y >= 0:
    print(int(x), int(y))
else:
    print(-1)

