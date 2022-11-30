n = int(input())

if n < 10:
    init_str_n = str(n).zfill(2)
else:
    init_str_n = str(n)
str_n = init_str_n

cnt = 0
while True:
    cnt+=1
    r_n = int(str_n[0])+int(str_n[1])
    str_n = str_n[1]+str(r_n)[-1]
    if str_n == init_str_n:
        print(cnt)
        break