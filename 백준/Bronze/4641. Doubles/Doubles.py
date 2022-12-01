
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '-1':
        break
    else:
        n = [int(i) for i in n.split(" ")]
        cnt = 0
        for i in n:
            for j in n:
                if j != 0 and i/j == 2:
                    cnt += 1
        print(cnt)