
import sys

n1 = int(sys.stdin.readline().rstrip())
n2 = int(sys.stdin.readline().rstrip())

if n1 > n2:
    r = 360-n1+0+n2
    l = n2 - n1
else:
    r = n2 - n1
    l = 0-n1+n2-360

if abs(r) <= abs(l):
    print(r)
else:
    print(l)
