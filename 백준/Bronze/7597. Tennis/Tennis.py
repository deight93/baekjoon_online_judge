
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == "#":
        break
    else:
        a, b = 0, 0
        a_s, b_s = 0, 0
        for i in s:
            if i == "A":
                a += 1
            else:
                b += 1

            if a >= b+2 and a >= 4:
                a_s += 1
                a, b = 0, 0

            if b >= a+2 and b >= 4:
                b_s += 1
                a, b = 0, 0

        print("A", a_s, "B", b_s)


