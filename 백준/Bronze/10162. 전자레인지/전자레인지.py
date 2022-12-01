import sys

t = int(sys.stdin.readline())

A = 60*5
B = 60*1
C = 10

A_cnt = 0
B_cnt = 0
C_cnt = 0

while True:
    if t >= A:
        A_cnt = A_cnt + (t // A)
        t = t % A
    else:
        if t >= B:
            B_cnt = B_cnt + (t // B)
            t = t % B

        else:
            if t >= C:
                C_cnt = C_cnt + (t // C)
                t = t % C
            else:
                if t != 0:
                    print(-1)
                else:
                    print(A_cnt, B_cnt, C_cnt)
                break