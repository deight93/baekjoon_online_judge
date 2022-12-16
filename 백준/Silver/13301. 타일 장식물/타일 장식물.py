import sys

n = int(sys.stdin.readline().rstrip())
t_1 = 1
t_2 = 1

if n == 1:
    print(n*4)
else:
    for i in range(1, n):
        temp = t_2
        t_2 += t_1
        t_1 = temp

    print(t_1*2+t_2*2)

