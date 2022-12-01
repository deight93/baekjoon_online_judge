
import sys

while True:
    l_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if l_list[0] == 0:
        break
    else:
        t = 1
        for i, v in enumerate(l_list[1:]):
            if i%2 == 0:
                t *= v
            else:
                t -= v
        print(t)
