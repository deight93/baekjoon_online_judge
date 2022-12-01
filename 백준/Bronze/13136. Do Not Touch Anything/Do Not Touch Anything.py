
import sys
import math

r, c, n = map(int, sys.stdin.readline().rstrip().split(" "))

print(math.ceil(r/n) * math.ceil(c/n))

