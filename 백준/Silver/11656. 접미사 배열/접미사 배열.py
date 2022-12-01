import sys

s = sys.stdin.readline().rstrip()
a = sorted([s[i:] for i in range(len(s))])
[print(i) for i in a]