import sys

while True:
    input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if input_list[0] == 0 and input_list[1] == 0:
        break

    a = input_list[0] // input_list[1]
    b = input_list[0] % input_list[1]

    print("{} {} / {}".format(a, b, input_list[1]))