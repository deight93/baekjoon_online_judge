import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    d, n, s, p = map(int, sys.stdin.readline().rstrip().split(" "))

    a = d+(n*p)
    b = n*s

    if a > b:
        print("do not parallelize")
    elif a < b:
        print("parallelize")
    else:
        print("does not matter")