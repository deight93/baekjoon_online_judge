import sys

input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

i_b = input_list[0]+input_list[1]
n_b = input_list[2]

cnt = 0
while True:
    a = i_b // n_b
    b = i_b % n_b

    t_b = a+b
    cnt += a
    if t_b < n_b:
        break
    else:
        i_b = t_b

print(cnt)

