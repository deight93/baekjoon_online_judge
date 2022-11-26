import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())
s = int(sys.stdin.readline().rstrip())

nikky = 0
byron = 0
c_s = s
ck = 0
while True:
    if ck % 2 == 0:
        nikky += a
        ck += 1
        c_s -= a
    else:
        nikky -= b
        ck += 1
        c_s -= b

    if c_s <= 0:
        if ck % 2 != 0:
            nikky -= a
            nikky += (a+c_s)
        else:
            nikky += b
            nikky -= (b+c_s)
        ck = 0
        c_s = s
        break

while True:
    if ck % 2 == 0:
        byron += c
        ck += 1
        c_s -= c
    else:
        byron -= d
        ck += 1
        c_s -= d

    if c_s <= 0:
        if ck % 2 != 0:
            byron -= c
            byron += (c+c_s)
        else:
            byron += d
            byron -= (d+c_s)
        break

if nikky > byron:
    print("Nikky")
elif nikky < byron:
    print("Byron")
else:
    print("Tied")
