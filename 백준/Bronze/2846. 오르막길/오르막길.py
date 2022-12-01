import sys

n = int(sys.stdin.readline())
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

f_s = input_list[0]
l_s = input_list[0]
temp = []
for i in input_list:
    if i > l_s:
        l_s = i
    else:
        f_s = i
        l_s = i
    temp += [l_s-f_s]
print(max(temp))