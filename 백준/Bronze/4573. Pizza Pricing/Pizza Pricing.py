
import sys

cnt = 0
while True:
    cnt += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        temp = []
        for _ in range(n):
            d, p = map(int, sys.stdin.readline().rstrip().split(" "))
            temp += [(d, p/((1/2)*d)**2*3.14)]
        print("Menu {}: {}".format(cnt, min(temp, key=lambda x:x[1])[0]))

