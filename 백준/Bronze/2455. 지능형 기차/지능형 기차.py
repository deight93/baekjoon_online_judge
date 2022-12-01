
import sys

input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(4)]

total_list = []
init = 0
max = 0
for i in input_list:
    init = init - i[0] + i[1]
    if init > max:
        max = init

print(max)