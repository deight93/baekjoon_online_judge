c = int(input())

for i in range(c):
    input_list = [int(i) for i in input().split(" ")]
    h = input_list[0]
    w = input_list[1]
    n = input_list[2]
    cnt = 0
    ck = False
    for j in range(1, w+1):
        for k in range(1, h+1):
            cnt += 1
            if cnt == n:
                print(str(k)+str(j).zfill(2))
                ck = True
                break
        if ck is True:
            break