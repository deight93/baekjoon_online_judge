import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

    ck = False
    m = 0
    for j in range(101):
        if a*15/100+b*20/100+c*25/100+j*40/100 >= 90:
            m = j
            ck = True
            break

    if ck is True:
        print(j)
    else:
        print("impossible")

