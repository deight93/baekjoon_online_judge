
import sys

while True:
    m, n = map(int, sys.stdin.readline().rstrip().split(" "))
    if m == 0 and n == 0:
        break
    else:
        k_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        cnt = 0
        for _ in range(n):
            k_list1 = list(map(int, sys.stdin.readline().rstrip().split(" ")))
            ck = True
            for i, j in zip(k_list, k_list1):
                if i < j:
                    ck = False
                    break
            if ck is True:
                cnt += 1
        print(cnt)