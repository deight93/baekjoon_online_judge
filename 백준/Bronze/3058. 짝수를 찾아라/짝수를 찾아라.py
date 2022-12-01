import sys

t = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(t)]

temp = []
for i in input_list:
    a = [j for j in i if j % 2 == 0]
    temp += [(sum(a), min(a))]

[print(i[0], i[1]) for i in temp]

