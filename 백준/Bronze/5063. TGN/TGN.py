import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().split()]
    r = input_list[0]
    e = input_list[1]
    c = input_list[2]

    if e > r+c:
        print("advertise")
    elif e == r+c:
        print("does not matter")
    elif e < r+c:
        print("do not advertise")