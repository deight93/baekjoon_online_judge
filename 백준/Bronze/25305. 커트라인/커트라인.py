import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
x = sorted(map(int, sys.stdin.readline().rstrip().split(" ")), reverse=True)
print(x[k-1])