
import sys

n = int(sys.stdin.readline())
p_list = []
for i in range(n):
    p, m = map(int, sys.stdin.readline().rstrip().split(" "))
    input_list = [int(sys.stdin.readline().rstrip()) for _ in range(p)]
    temp = [0 for _ in range(m)]

    cnt = 0
    for i in input_list:
        if temp[i-1] != 0:
            cnt += 1
        else:
            temp[i-1] = i

    p_list += [cnt]

[print(_) for _ in p_list]