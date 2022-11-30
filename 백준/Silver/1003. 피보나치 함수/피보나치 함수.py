import sys

n = int(sys.stdin.readline().rstrip())
input_list = [int(sys.stdin.readline()) for i in range(n)]

for j in input_list:
    if j == 0:
        init1 = [1, 0]
    elif j == 1:
        init1 = [0, 1]
    elif j == 2:
        init1 = [1, 1]
    else:
        init1 = [1, 0]
        for i in range(j):
            temp3 = [init1[1], init1[0] + init1[1]]
            init1 = temp3
    print(init1[0], init1[1])