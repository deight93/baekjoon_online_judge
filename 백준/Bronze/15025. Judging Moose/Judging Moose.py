import sys

l, r = map(int, sys.stdin.readline().rstrip().split(" "))

if l == r:
    b = l+r
    eo = "Even"
else:
    b = max([l, r])*2
    eo = "Odd"

if b == 0:
    print("Not a moose")
else:
    print(eo, b)
