import sys

input_list = [int(i) for i in sys.stdin.readline().split()]

k = input_list[0]
n = input_list[1]
m = input_list[2]

total = k*n

if m >= total:
    print(0)
else:
    print(total-m)