import sys

n = int(sys.stdin.readline().rstrip())

input_list = [sys.stdin.readline().rstrip() for _ in range(n)]
temp_dict = {}

for i in input_list:
    temp_dict[i] = [len(i)]
    temp = 0
    for j in i:
        if j.isnumeric() is True:
            temp += int(j)
    temp_dict[i] += [temp]

[print(i[0]) for i in sorted(temp_dict.items(), key=lambda x: (x[1][0], x[1][1], x[0]))]