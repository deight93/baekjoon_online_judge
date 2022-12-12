import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
if c % 2 == 0:
    print((a^b)^b)
else:
    print(a^b)

