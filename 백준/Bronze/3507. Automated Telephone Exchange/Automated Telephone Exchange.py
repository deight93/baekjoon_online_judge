import sys

n = int(sys.stdin.readline().rstrip())
r = 0

if n > 199:
    print(r)
else:
    for j in range(1, 100):
        for k in range(1, 100):
            if n-j-k == 0:
                r += 1
    print(r)
