import sys

c, k = map(int, sys.stdin.readline().rstrip().split(" "))

print(int(round(c+0.001, -1*k)))
