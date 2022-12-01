import sys

t = int(sys.stdin.readline().rstrip())
temp3 = []
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]
    temp = {}
    for i in input_list:
        if i[1] in temp.keys():
            temp[i[1]] += [i[0]]
        else:
            temp[i[1]] = [i[0]]

    a = [len(v)+1 for k, v in temp.items()]
    temp2 = 1
    for i in a:
        temp2 *= i

    temp3+= [temp2-1]

[print(i) for i in temp3]