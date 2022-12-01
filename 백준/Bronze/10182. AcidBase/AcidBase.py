
import sys
import math

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k, v = sys.stdin.readline().rstrip().split(" = ")
    v = -1*math.log10(float(v))
    if k == "H":
        print("{:.2f}".format(v))
    else:
        print("{:.2f}".format(14-v))

