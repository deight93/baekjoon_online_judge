import sys

h, p = map(int, sys.stdin.readline().rstrip().split(" "))
print(min(h//2, p))