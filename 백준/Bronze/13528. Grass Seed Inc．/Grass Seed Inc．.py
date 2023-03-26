import sys

c = float(sys.stdin.readline().strip())
r = 0
for i in range(int(sys.stdin.readline().strip())):
    w, l = map(float, sys.stdin.readline().strip().split(" "))
    r += c * w * l
print(r)