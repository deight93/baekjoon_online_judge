import sys

t = int(sys.stdin.readline())
for c in range(t):
    input_list = [int(i) for i in sys.stdin.readline().split(" ")]
    x1 = input_list[0]
    y1 = input_list[1]
    r1 = input_list[2]

    x2 = input_list[3]
    y2 = input_list[4]
    r2 = input_list[5]

    d = (x1-x2)**2 + (y1-y2)**2

    if d**0.5 == 0 and r1 == r2:
        print(-1)
    else:
        if abs(r2-r1) < d**0.5 < abs(r2+r1):
            print(2)
        elif abs(r2+r1) == d**0.5:
            print(1)
        elif abs(r2-r1) == d**0.5:
            print(1)
        elif abs(r2 - r1) > d**0.5:
            print(0)
        elif abs(r2 + r1) < d**0.5:
            print(0)

