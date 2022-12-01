
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == 'END':
        break
    else:
        ck = True
        for i in range(65, 91):
            if n.count(chr(i)) >= 2:
                ck = False
                break

        if ck is True:
            print(n)

