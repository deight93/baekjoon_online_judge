import sys

input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

while True:
    a1 = input_list[0]
    a2 = input_list[1]
    if input_list[0] > input_list[1]:
        input_list[0] = a2
        input_list[1] = a1
        for i in input_list:
            print(i, end=" ")
        print()

    a2 = input_list[1]
    a3 = input_list[2]
    if input_list[1] > input_list[2]:
        input_list[1] = a3
        input_list[2] = a2
        for i in input_list:
            print(i, end=" ")
        print()

    a3 = input_list[2]
    a4 = input_list[3]
    if input_list[2] > input_list[3]:
        input_list[2] = a4
        input_list[3] = a3
        for i in input_list:
            print(i, end=" ")
        print()

    a4 = input_list[3]
    a5 = input_list[4]
    if input_list[3] > input_list[4]:
        input_list[3] = a5
        input_list[4] = a4
        for i in input_list:
            print(i, end=" ")
        print()

    if input_list == [1, 2, 3, 4, 5]:
        break