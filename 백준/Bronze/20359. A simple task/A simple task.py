import sys

n = int(sys.stdin.readline().rstrip())
o = n
p = 0

while True:
    if o % 2 == 0:
        p += 1
        o = o//2
    else:
        break

print(o, p)