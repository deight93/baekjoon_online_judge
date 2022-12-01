import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
m = (b-a)/400
r = 1/(1+(10**m))
print(r)

