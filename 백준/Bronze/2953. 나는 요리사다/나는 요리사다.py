import sys

input_list = [sum([int(j) for j in sys.stdin.readline().rstrip().split(" ")]) for i in range(5)]
print(input_list.index(max(input_list))+1, max(input_list))