import sys

input_list = sorted([int(sys.stdin.readline().rstrip()) for i in range(5)])
avg = int(sum(input_list)/len(input_list))

print(avg)
print(input_list[len(input_list)//2])