import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(10)]

avg = int(sum(input_list)/len(input_list))
mode = max([(i, input_list.count(i)) for i in input_list], key=lambda x: x[1])
print(avg)
print(mode[0])