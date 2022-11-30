x = int(input())
c_x = x
cnt = 0
total_cnt = 0
while True:
    cnt += 1
    c_x -= cnt
    if c_x <= 0:
        break
    total_cnt += cnt

cnt = cnt-1
x_c = total_cnt
ck = True
while True:
    if ck is False:
        break
    cnt += 1
    for i in range(1, cnt+1):
        if divmod(cnt, 2)[1] == 1:
            a = cnt+1-i
            b = i
        else:
            a = i
            b = cnt+1-i
        x_c += 1

        if x == x_c:
            print("{}/{}".format(a, b))
            ck = False
            break