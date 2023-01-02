import sys

n = int(sys.stdin.readline().rstrip())
ni = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(ni.index(min(ni)))

