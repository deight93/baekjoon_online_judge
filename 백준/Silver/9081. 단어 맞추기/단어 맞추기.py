import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    input_list = [i for i in s]
    n = len(s)

    max_i = n+1
    for i in range(0, n-1):
        if input_list[i] < input_list[i+1]:
            max_i = i

    if max_i == n+1:
        print(s)
    else:
        max_j = 0
        for j in input_list[max_i:]:
            if j > input_list[max_i]:
                max_j = input_list.index(j, max_i, len(s))

        a = input_list[max_i]
        b = input_list[max_j]
        input_list[max_j] = a
        input_list[max_i] = b

        input_list[max_i+1:] = sorted(input_list[max_i+1:])
        print("".join([str(i) for i in input_list]))