import sys

input_list = max([sum([int(i) for i in sys.stdin.readline().rstrip().split(" ")]) for _ in range(2)])
print(input_list)