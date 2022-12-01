import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in input_list:
    if i[1] == "kg":
        print("{:.4f} lb".format(float(i[0])*2.2046))
    elif i[1] == "l":
        print("{:.4f} g".format(float(i[0]) * 0.2642))
    elif i[1] == "lb":
        print("{:.4f} kg".format(float(i[0]) * 0.4536))
    elif i[1] == "g":
        print("{:.4f} l".format(float(i[0]) * 3.7854))