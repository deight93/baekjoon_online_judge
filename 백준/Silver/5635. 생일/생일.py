import sys
import datetime

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

init = datetime.datetime(year=int(input_list[0][3]), month=int(input_list[0][2]), day=int(input_list[0][1]))
min = init
max = init
min_n = input_list[0][0]
max_n = input_list[0][0]
for i in input_list[1:]:
    temp = datetime.datetime(year=int(i[3]), month=int(i[2]), day=int(i[1]))
    if temp < min:
        min = temp
        min_n = i[0]

    if temp > max:
        max = temp
        max_n = i[0]
print(max_n)
print(min_n)