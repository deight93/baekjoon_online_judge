
import sys

while True:
    l, w, h, v = map(int, sys.stdin.readline().rstrip().split(" "))
    if [l, w, h, v] == [0, 0, 0, 0]:
        break

    if v == 0:
        print(l, w, h, l*w*h)
    elif l == 0:
        print(v//(w*h), w, h, v)
    elif w == 0:
        print(l, v // (l * h), h, v)
    elif h == 0:
        print(l, w, v // (w * l), v)
