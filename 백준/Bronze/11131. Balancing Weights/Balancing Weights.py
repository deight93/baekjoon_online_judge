
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    wn = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    r = sum(wn)

    if r == 0:
        print("Equilibrium")
    elif r > 0:
        print("Right")
    elif r < 0:
        print("Left")





