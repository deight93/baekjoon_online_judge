
import sys

cnt = 0
while True:
    cnt += 1
    l, p, v = map(int, sys.stdin.readline().rstrip().split(" "))
    if l == 0 and p == 0 and v == 0:
        break
    else:
        a = (v//p)*l
        b = v-((v//p)*p)
        if b >= l:
            b = l

        print("Case {}: {}".format(cnt, a + b))
