import sys

input_list = [int(i) for i in sys.stdin.readline().split(" ")]

total = input_list[0]
avg = input_list[1]-1

m = total*avg+1
print(m)