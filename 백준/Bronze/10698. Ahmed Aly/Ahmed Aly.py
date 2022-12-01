import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_list = [i for i in sys.stdin.readline().rstrip().split(" ")]

    if input_list[1] == "+":
        if int(input_list[0])+int(input_list[2]) == int(input_list[4]):
            print("Case {}: YES".format(i+1))
        else:
            print("Case {}: NO".format(i+1))

    elif input_list[1] == "-":
        if int(input_list[0]) - int(input_list[2]) == int(input_list[4]):
            print("Case {}: YES".format(i+1))

        else:
            print("Case {}: NO".format(i+1))