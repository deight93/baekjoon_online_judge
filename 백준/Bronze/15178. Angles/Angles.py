import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b, c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if sum([a, b, c]) == 180:
        print(a, b, c, "Seems OK")
    else:
        print(a, b, c, "Check")