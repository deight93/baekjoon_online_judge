input_list = [int(i) for i in input().split(" ")]

x = input_list[0]
y = input_list[1]
w = input_list[2]
h = input_list[3]

d1 = x
d2 = abs(w-x)
d3 = y
d4 = abs(h-y)

print(min(d1, d2, d3, d4))