
import sys

k = int(sys.stdin.readline().rstrip())
d1, d2 = map(int, sys.stdin.readline().rstrip().split(" "))

if d1 == d2:
    print(k**2)
else:
    t = (max([d1, d2]) - min([d1, d2]))/2
    h = k**2 - t**2
    print(h)

