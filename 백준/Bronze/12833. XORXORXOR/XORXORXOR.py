import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
if c % 2 != 0:
    a ^= b

print(a)


