
import sys

while True:
    name = sys.stdin.readline().rstrip().split(" ")
    if all("#" == i for i in name):
        break

    n = int(sys.stdin.readline().rstrip())
    cnt = [0, 0]
    for _ in range(n):
        c1, c2 = sys.stdin.readline().rstrip().split(" ")
        if c1 == c2:
            cnt[0] += 1
        else:
            cnt[1] += 1

    print("{} {} {} {}".format(name[0], cnt[0], name[1], cnt[1]))

