
import sys


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        s = map(int, sys.stdin.readline().rstrip().split(" "))
        m = 0
        j = 0

        for i in s:
            if i == 0:
                m += 1
            else:
                j += 1
        print("Mary won {} times and John won {} times".format(m, j))


