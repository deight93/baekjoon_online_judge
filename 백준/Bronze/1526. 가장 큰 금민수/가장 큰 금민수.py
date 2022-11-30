
import sys

n = int(sys.stdin.readline().rstrip())

while True:
    ck = True
    for i in str(n):
        if i != "4" and i != "7":
            ck = False
            n -= 1

    if ck:
        print(n)
        break