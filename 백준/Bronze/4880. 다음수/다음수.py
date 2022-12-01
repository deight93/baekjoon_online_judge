import sys

temp = []
while True:
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    if input_list[0] == 0 and input_list[1] == 0 and input_list[2] == 0:
        break
    temp += [input_list]


for i in temp:
    a = i[1]-i[0]
    b = i[2]-i[1]
    if a == b:
        print("AP {}".format(i[-1]+a))
    else:
        if i.count(0) != 0:
            if i[0] == 0:
                c = i[2] / i[1]
                print("GP {}".format(int(i[-1]*c)))
            elif i[1] == 0:
                c = i[2] / i[0]
                c = int(c**0.5)
                print("GP {}".format(int(i[-1]*c)))
            elif i[2] == 0:
                c = i[1] / i[0]
                print("GP {}".format(int(i[-1]*c)))
        elif i.count(0) == 0:
            c = i[2] / i[1]
            d = i[1] / i[0]
            print("GP {}".format(int(i[-1] * c)))