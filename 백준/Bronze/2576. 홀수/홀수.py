import sys

input_list = [int(sys.stdin.readline().rstrip()) for i in range(7)]
input_list2 = [i for i in input_list if i%2 == 1]

if input_list2:
    print(sum(input_list2))
    print(min(input_list2))
else:
    print(-1)