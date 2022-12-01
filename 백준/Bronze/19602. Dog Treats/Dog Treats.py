import sys

s, m, l = [int(sys.stdin.readline().rstrip()) for _ in range(3)]
if (1*s) + (2*m) + (3*l) >= 10:
    print("happy")
else:
    print("sad")