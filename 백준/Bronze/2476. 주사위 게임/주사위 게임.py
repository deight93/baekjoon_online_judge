import sys

n = int(sys.stdin.readline())

temp_list = []
for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().split()]

    if len(set(input_list)) == 1:
        temp = 10000+input_list[0]*1000
    elif len(set(input_list)) == 2:
        set_list = list(set(input_list))
        input_list.remove(set_list[0])
        input_list.remove(set_list[1])
        temp = 1000+input_list[0]*100
    else:
        temp = max(input_list)*100

    temp_list += [temp]
print(max(temp_list))