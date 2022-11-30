import sys

a = sum(map(lambda x: int("0b"+x, 2), sys.stdin.readline().rstrip().split(" ")))
print(format(a, 'b'))
