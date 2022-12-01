import sys

ss = [4.5, 6.0, 5.0]
mw = [150, 300, 200]
ms = [200, 500, 300]

while True:
    a, b, c = sys.stdin.readline().rstrip().split(" ")
    a = float(a)
    b = int(b)
    c = int(c)
    r = []

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a <= ss[0] and b >= mw[0] and c >= ms[0]:
            r += ["Wide Receiver"]
        if a <= ss[1] and b >= mw[1] and c >= ms[1]:
            r += ["Lineman"]
        if a <= ss[2] and b >= mw[2] and c >= ms[2]:
            r += ["Quarterback"]

        if not r:
            print("No positions")
        else:
            print(" ".join(r))

