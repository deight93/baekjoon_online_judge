
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    else:
        t = 0
        for k, i in enumerate(n):
            a = int(i)
            for j in [j for j in range(1, len(n)-k+1)]:
                a = a*j
            t += a
        print(t)