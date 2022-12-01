import sys

n, w, h, l = map(int, sys.stdin.readline().rstrip().split(" "))

if (w//l) * (h//l) >= n:
    print(n)
else:
    print((w//l)*(h//l))

