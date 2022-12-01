import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
print(min(n//2, m//2))