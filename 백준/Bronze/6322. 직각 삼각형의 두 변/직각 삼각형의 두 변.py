import sys

temp = []
while True:
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    if input_list[0] == 0 and input_list[1] == 0 and input_list[2] == 0:
        break
    temp += [input_list]

cnt = 0
for i in temp:
    cnt += 1
    print("Triangle #{}".format(cnt))

    a = i[0]
    b = i[1]
    c = i[2]

    if a == -1:
        if b >= c:
            print("Impossible.")
        else:
            a = (c**2-b**2)**0.5
            print("a = {:.3f}".format(a))
        print()
    elif b == -1:
        if a >= c:
            print("Impossible.")
        else:
            b = (c**2-a**2)**0.5
            print("b = {:.3f}".format(b))
        print()
    elif c == -1:
        c = (a**2+b**2)**0.5
        print("c = {:.3f}".format(c))
        print()