
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    total = 0
    for i in range(2, n+2):
        a = (i*(i+1))/2
        total += a*(i-1)
    print(int(total))