import sys

while True:
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    if input_list[0] == 0 and input_list[1] == 0:
        break

    a = input_list[0]
    b = input_list[1]

    x = (a*2)-b
    print(x)