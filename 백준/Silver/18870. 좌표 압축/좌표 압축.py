import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
sort_input_list = sorted(set(input_list))

temp = {sort_input_list[i]:i for i in range(len(sort_input_list))}

for i in input_list:
    print(temp[i], end = ' ')