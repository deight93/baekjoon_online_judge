import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline()) for i in range(n)]


if n == 1:
    max_s_list = [input_list[0]]
elif n == 2:
    max_s_list = [input_list[0]]
    max_s_list += [max(input_list[0]+input_list[1], input_list[1])]
else:
    max_s_list = [input_list[0]]
    max_s_list += [max(input_list[0]+input_list[1], input_list[1])]
    max_s_list += [max(input_list[0]+input_list[2], input_list[1]+input_list[2])]

    for i in range(3, n):
        max_s_list += [max(max_s_list[i-2] + input_list[i] , max_s_list[i-3] + input_list[i] + input_list[i - 1])]

print(max_s_list.pop())