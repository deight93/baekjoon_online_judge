import sys

while True:
    a, b = sys.stdin.readline().rstrip().split(" ")

    if a == '0' and b == '0':
        break
    else:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        ck_c = 0
        c_cnt = 0
        for i in range(max_len):
            if ck_c == 0:
                if int(a[::-1][i])+int(b[::-1][i]) >= 10:
                    c_cnt += 1
                    ck_c = 1
                else:
                    ck_c = 0
            else:
                if int(a[::-1][i]) + int(b[::-1][i])+1 >= 10:
                    c_cnt += 1
                    ck_c = 1
                else:
                    ck_c = 0
        print(c_cnt)
