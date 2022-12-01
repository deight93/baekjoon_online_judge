
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

if a != b:
    print(max([a, b]))
else:
    print(a)