
import math
import sys

r = int(sys.stdin.readline())
t = r**2*2
u = r**2*math.pi

print("{:.6f}".format(round(u, 6)))
print("{:.6f}".format(t))
