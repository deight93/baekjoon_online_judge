import sys

n, h, v = map(int, sys.stdin.readline().rstrip().split(" "))
print(4 * max(n-h, h) * max(n-v, v))

