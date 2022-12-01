import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b, c, d, e = map(float, sys.stdin.readline().rstrip().split(" "))
    print("{} {:.6f}".format(int(a), b / (c+d)*e))
