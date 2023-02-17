import sys
import math

s = int(sys.stdin.readline().rstrip())
r = (s/math.pi)**0.5
print(r*2*math.pi)