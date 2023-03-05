import sys

while True:
    n, m = map(int, sys.stdin.readline().rstrip().split(" "))
    temp_dict = {}
    if n == 0 and m == 0:
        break
    else:
        ti = map(int, sys.stdin.readline().rstrip().split(" "))
        for i in ti:
            if i in temp_dict.keys():
                temp_dict[i] += 1
            else:
                temp_dict[i] = 1
        cnt = 0
        for k, v in temp_dict.items():
            if v > 1:
                cnt += 1
        print(cnt)
