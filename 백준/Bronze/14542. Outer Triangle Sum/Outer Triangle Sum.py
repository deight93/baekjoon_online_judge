import sys

cnt = 0
while True:
    cnt += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        t = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]
        s = 0
        for i in range(n):
            if i == 0:
                s += sum(t[i])
            elif i == n-1:
                s += sum(t[i])
            else:
                s += t[i][0]
                s += t[i][-1]

        print("Case #{}:{}".format(cnt, s))







