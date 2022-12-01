
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if int(n) == 0:
        break
    else:
        temp = [n]
        while True:
            if len(n) == 1:
                break
            else:
                a = 1
                for i in n:
                    a *= int(i)
                temp += [str(a)]
                n = str(a)
        print(" ".join(temp))