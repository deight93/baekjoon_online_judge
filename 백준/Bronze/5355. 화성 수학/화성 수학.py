import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_list = [i for i in sys.stdin.readline().split()]
    temp = float(input_list[0])
    for j in input_list[1:]:
        if j == "@":
            temp *= 3
        elif j == "%":
            temp += 5
        elif j == "#":
            temp -= 7
    print("{:.2f}".format(round(temp, 3)))