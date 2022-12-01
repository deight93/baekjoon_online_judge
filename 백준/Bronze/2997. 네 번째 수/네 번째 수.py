import sys

input_list = sorted(map(int, sys.stdin.readline().rstrip().split(" ")))
temp = [input_list[1]-input_list[0], input_list[2]-input_list[1]]

if len(set(temp)) == 1:
    print(input_list[2]+temp[0])
else:
    if temp[0] < temp[1]:
        print(input_list[1] + temp[0])
    else:
        print(input_list[0] + temp[1])