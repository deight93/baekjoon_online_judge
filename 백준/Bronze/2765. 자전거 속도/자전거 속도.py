import math
import sys

cnt = 0
while True:
    cnt += 1
    a, b, c = map(float, sys.stdin.readline().rstrip().split(" "))
    if b == 0:
        break

    d = (math.pi*a*b)/63360
    mph = d/c*3600
    print("Trip #{}: {:.2f} {:.2f}".format(cnt, d, mph))


