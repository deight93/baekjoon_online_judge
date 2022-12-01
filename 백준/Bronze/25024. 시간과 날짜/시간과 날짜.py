import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    r1 = "No"
    if x <= 23 and y <= 59:
        r1 = "Yes"

    r2 = "No"
    if 1 <= x <= 12:
        if x in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= y <= 31:
                r2 = "Yes"
        elif x == 2:
            if 1 <= y <= 29:
                r2 = "Yes"
        else:
            if 1 <= y <= 30:
                r2 = "Yes"

    print("{} {}".format(r1, r2))

