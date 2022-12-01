
import sys

cnt = 0
while True:
    cnt += 1
    temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if len(temp) == 1 and temp[0] == 0:
        break
    else:
        r, w, l = temp

        if (w**2+l**2)**0.5 <= 2*r:
            print("Pizza {} fits on the table.".format(cnt))
        else:
            print("Pizza {} does not fit on the table.".format(cnt))


