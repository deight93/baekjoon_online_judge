import sys

input_list = [sys.stdin.readline().rstrip() for i in range(3)]

if input_list[1] == '*':
    print(int(input_list[0]) * int(input_list[2]))
else:
    print(int(input_list[0]) + int(input_list[2]))