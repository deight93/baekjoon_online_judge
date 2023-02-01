import sys

k = int(sys.stdin.readline().rstrip())
a, b, c, d = map(int, sys.stdin.readline().rstrip().split(" "))

if a*k+b == c*k+d:
    print("Yes", c*k+d)
else:
    print("No")