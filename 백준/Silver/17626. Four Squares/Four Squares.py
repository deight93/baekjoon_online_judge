import sys

n = int(sys.stdin.readline().rstrip())
d = [i for i in range(n+1)]
d[0] = 0
for i in range(1, n+1):
    j = 1
    while True:
        if i - (j * j) < 0:
            break

        d[i] = min(d[i], d[i - (j*j)]+1)
        j += 1

print(d[n])
