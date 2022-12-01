
import sys

n = int(sys.stdin.readline().rstrip())
input_list = [sys.stdin.readline().rstrip() for i in range(n)]

for i in input_list:
    temp_list = []
    len_i = int(len(i)**0.5)
    for j in range(len_i):
        temp_list += [i[j*len_i:(j+1)*len_i]]

    temp = ""
    for j in range(len_i):
        for k in temp_list:
            temp += k[len_i-j-1]
    print(temp)
