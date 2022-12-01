
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    t = []
    while True:
        t.append(n)
        if n == 1:
            break

        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    print(max(t))