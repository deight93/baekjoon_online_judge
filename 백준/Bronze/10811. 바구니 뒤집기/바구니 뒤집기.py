import sys
n, m = map(int, sys.stdin.readline().rstrip().split(" "))

b_list = [i+1 for i in range(n)]

input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(m)]

for i in input_list:
    for j in range(int((i[1]-i[0]+1)/2)):
        a = i[0]+j
        b = i[1]-j
        a1 = b_list[a-1]
        b1 = b_list[b-1]
        b_list[a - 1] = b1
        b_list[b - 1] = a1

[print(i, end=" ") for i in b_list]