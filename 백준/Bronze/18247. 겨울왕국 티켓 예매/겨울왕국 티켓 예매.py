import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    if n <= 11 or m <= 3:
        print(-1)
    else:
        print(m*11+4)

