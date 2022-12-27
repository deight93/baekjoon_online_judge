import sys
from itertools import permutations

ix, iy = map(int, sys.stdin.readline().rstrip().split(" "))
xy = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(3)]

temp = []
for i in list(permutations(xy, 3)):
    iix, iiy = ix, iy
    t = 0
    for j in i:
        t += ((iix-j[0])**2+(iiy-j[1])**2)**0.5
        iix = j[0]
        iiy = j[1]
    temp += [t]
print(int(min(temp)))
# print("{:.0f}".format(min(temp)))
