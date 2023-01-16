import sys

m, seed, x1, x2 = map(int, sys.stdin.readline().rstrip().split(" "))
ck = False

for a in range(100):
    for c in range(100):
        if ((a*seed)+c) % m == x1 and ((a*x1)+c) % m == x2:
            ck = True
            print(a, c)
            break
    if ck is True:
        break
