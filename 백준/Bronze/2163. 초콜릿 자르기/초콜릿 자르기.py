import sys

input_list = [int(i) for i in sys.stdin.readline().split(" ")]
a = input_list[0]
b = input_list[1]

x = (a-1)+(a*(b-1))
print(x)