import sys

n, x = map(int, sys.stdin.readline().rstrip().split(" "))
tn = list(map(int, sys.stdin.readline().rstrip().split(" ")))

cnt = 0
while True:
    if x > tn[cnt % n]:
        print((cnt % n)+1)
        break
    x += 1
    cnt += 1

