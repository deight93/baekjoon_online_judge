
import sys

while True:
    d, rh, rv = map(float, sys.stdin.readline().rstrip().split(" "))

    if not all([d, rh, rv]):
        break

    w = (16*d)/(337**0.5)
    h = (9/16)*w
    print("Horizontal DPI: {:.2f}".format(rh/w))
    print("Vertical DPI: {:.2f}".format(rv/h))
