import sys

n = int(sys.stdin.readline().rstrip())
print(sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))[-1])
