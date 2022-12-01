
while True:
    cnt = 0
    n = int(input())
    n_2 = n*2
    if n == 0:
        break

    temp = [i for i in range(2, int(n_2**0.5)+1)]
    temp2 = [True for i in range(n_2+1)]

    for i in temp:
        if temp2[i] is True:
            for j in range(i+i, n_2+1, i):
                temp2[j] = False

    temp3 = [i for i in range(2, n_2+1) if temp2[i] == True]
    print(len([i for i in temp3 if i > n]))