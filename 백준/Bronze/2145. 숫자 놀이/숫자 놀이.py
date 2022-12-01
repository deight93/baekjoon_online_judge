
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    else:
        t = 0
        while True:
            for i in n:
                t += int(i)

            if len(str(t)) == 1:
                print(t)
                break
            else:
                n = str(t)
                t = 0
