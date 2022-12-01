import sys

input_list = [sys.stdin.readline().rstrip() for i in range(2)]

for i in range(10):
    input_list[0] = input_list[0].replace("{}".format(i), "")

if input_list[0].find(input_list[1]) != -1:
    print(1)
else:
    print(0)