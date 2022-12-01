import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

light = [0] * n

for _ in range(m):
    o, s_i, e_i = map(int, sys.stdin.readline().rstrip().split(" "))

    if o == 0:
        for i in range(s_i-1, e_i):
            if light[i] == 0:
                light[i] = 1
            else:
                light[i] = 0
    else:
        print(light[s_i-1:e_i].count(1))

