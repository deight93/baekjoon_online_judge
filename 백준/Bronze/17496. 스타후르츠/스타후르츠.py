import sys

n, t, c, p = map(int, sys.stdin.readline().rstrip().split(" "))
print(((n-1)//t)*c*p)

