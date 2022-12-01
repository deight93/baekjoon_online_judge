
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    b, p = map(float, sys.stdin.readline().rstrip().split(" "))
    print("{:.4f} {:.4f} {:.4f}".format((b-1)*(60/p), b*(60/p), (b+1)*(60/p)))

