import sys
import math

while True:
    xy = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    if sum(xy) == 0:
        break
    else:
        d1 = abs(0 - xy[0])
        d2 = abs(0 - xy[1])
        print(round(math.atan2(d2, d1) * 180 / math.pi))

