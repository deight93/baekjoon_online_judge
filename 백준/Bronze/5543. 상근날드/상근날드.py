import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(5)]

print(min(input_list[:3])+min(input_list[3:])-50)