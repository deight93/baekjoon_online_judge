
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    else:
        while True:
            temp = 0
            for i in n:
                temp += int(i)

            n = str(temp)
            if len(n) == 1:
                print(n)
                break