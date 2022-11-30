c = int(input())
input_list = [input() for i in range(c)]

cnt = 0
for i in input_list:
    temp = i[0]
    f_c = i[0]
    for j in i:
        if j == f_c:
            pass
        else:
            f_c = j
            temp += j

    if len(temp) == len(set(temp)):
        cnt += 1

print(cnt)