import sys

input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(max(input_list[1]-input_list[0]-1, input_list[2]-input_list[1]-1))