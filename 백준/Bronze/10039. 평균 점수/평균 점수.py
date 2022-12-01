import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(5)]
temp = [i if i >= 40 else 40 for i in input_list]

print(sum(temp)//len(temp))