import math

input_list = [int(i) for i in input().split(" ")]
a = input_list[0]
b = input_list[1]
v = input_list[2]

print(math.ceil((v-a)/(a-b))+1)