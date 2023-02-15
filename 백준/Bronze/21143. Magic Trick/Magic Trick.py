import sys

s = list(sys.stdin.readline().rstrip())

if len(s) == len(set(s)):
    print(1)
else:
    print(0)