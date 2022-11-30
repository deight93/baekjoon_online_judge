import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [set([int(j) for j in sys.stdin.readline().rstrip().split(" ")]) for _ in range(2)]
a_b = input_list[0]-input_list[1]
b_a = input_list[1]-input_list[0]
print(len(a_b)+len(b_a))