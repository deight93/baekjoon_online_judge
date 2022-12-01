n = int(input())
temp = [int(i) for i in input().split(" ")]

cnt = 0

if n == len(temp):
    for i in temp:
        if i <= 1:
            continue

        ck = True
        for j in range(2, i+1):
            if i % j == 0:
                if i == j and ck is True:
                    cnt += 1
                else:
                    ck = False
    print(cnt)