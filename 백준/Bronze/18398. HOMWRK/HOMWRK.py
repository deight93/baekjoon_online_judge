
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        a, b = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        print(a+b, a*b)
