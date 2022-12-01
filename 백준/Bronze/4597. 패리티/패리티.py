import sys

input_list = []
while True:
    n = sys.stdin.readline().rstrip()
    if n == "#":
        break
    else:
        input_list += [n]


for i in input_list:
    if i[-1] == "e":
        cnt = 0
        for j in i[:-1]:
            if j == "1":
                cnt += 1

        if cnt%2 == 0:
            temp = "0"
        else:
            temp = "1"
    else:
        cnt = 0
        for j in i[:-1]:
            if j == "1":
                cnt += 1

        if cnt%2 == 0:
            temp = "1"
        else:
            temp = "0"

    print(i[:-1]+temp)