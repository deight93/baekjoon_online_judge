import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_list = sorted([int(i) for i in sys.stdin.readline().rstrip().split(" ")])
    max_i = max(input_list)
    min_i = min(input_list)
    input_list.remove(max_i)
    input_list.remove(min_i)

    if max(input_list)-min(input_list) >= 4:
        print("KIN")
    else:
        print(sum(input_list))