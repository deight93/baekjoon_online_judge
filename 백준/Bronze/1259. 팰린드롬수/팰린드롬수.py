
import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    str_n = str(n)

    ck = True
    for i in range(int(len(str_n)/2)):
        if str_n[i] != str_n[len(str_n)-i-1]:
            ck = False
            continue

    if ck is True:
        print("yes")
    else:
        print("no")
