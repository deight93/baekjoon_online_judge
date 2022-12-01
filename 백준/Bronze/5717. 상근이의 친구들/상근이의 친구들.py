import sys


while True:
    input_list = [int(i) for i in sys.stdin.readline().split()]
    if input_list[0] == 0 and input_list[1] == 0:
        break

    print(sum(input_list))