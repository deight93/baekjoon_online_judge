import sys

cnt = 0
while True:
    cnt += 1
    ck = "even"
    n0 = int(sys.stdin.readline())
    if n0 == 0:
        break
    else:
        n1 = 3 * n0
        if n1 % 2 == 0:
            n2 = n1 / 2
        else:
            n2 = (n1 + 1) / 2
            ck = "odd"
        n3 = 3 * n2
        n4 = int(n3 // 9)

        print("{}. {} {}".format(cnt, ck, n4))