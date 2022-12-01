
import sys

a, b, c, d = map(int, sys.stdin.readline().rstrip().split(" "))
p_m_n = map(int, sys.stdin.readline().rstrip().split(" "))

for i in list(p_m_n):
    t1 = 0
    i1 = i
    while True:
        if i1-a <= 0:
            t1 += 1
            break
        elif i1-a-b <= 0:
            break
        else:
            i1 = i1-a-b

    t2 = 0
    i2 = i
    while True:
        if i2-c <= 0:
            t2 += 1
            break
        elif i2-c-d <= 0:
            break
        else:
            i2 = i2-c-d

    print(t1+t2)
