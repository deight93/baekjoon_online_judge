import sys

import math

n = int(sys.stdin.readline().rstrip())

r = (n/math.pi)**0.5

print(2*r*math.pi)

print("{:.10f}".format(2*r*math.pi))

