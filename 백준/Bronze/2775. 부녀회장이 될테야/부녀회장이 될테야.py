input_t = int(input())

for t in range(input_t):
    k = int(input())
    n = int(input())

    temp1 = [i for i in range(1, n + 1)]
    for j in range(k+1):
        temp2 = [1]
        for i in range(1, n):
            temp2 += [sum(temp1[:i+1])]

        if k == j:
            print(temp1[-1])
        else:
            temp1 = temp2