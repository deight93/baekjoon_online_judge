import sys

t = int(sys.stdin.readline())

for _ in range(t):
    p = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    temp = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        p += (a*b)
    print(p)
