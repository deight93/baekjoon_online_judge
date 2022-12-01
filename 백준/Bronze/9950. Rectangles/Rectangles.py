
import sys

while True:
    l, w, a = map(int, sys.stdin.readline().rstrip().split(" "))
    if [l, w, a] == [0, 0, 0]:
        break

    if a == 0:
        print(l, w, l*w)
    elif l == 0:
        print(a//w, w, a)
    elif w == 0:
        print(l, a//l, a)
