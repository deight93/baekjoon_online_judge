import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    if max(input_list) > sum(input_list)//2 and input_list.count(max(input_list)) == 1:
        print("majority winner {}".format(input_list.index(max(input_list))+1))
    elif max(input_list) <= sum(input_list)//2 and input_list.count(max(input_list)) == 1:
        print("minority winner {}".format(input_list.index(max(input_list))+1))
    else:
        print("no winner")