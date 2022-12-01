import sys

n, l = map(int, sys.stdin.readline().rstrip().split(" "))
str_l = str(l)

cn = 0
cnt = 0
while True:
    cn += 1
    if str_l not in str(cn):
        cnt += 1

    if cnt == n:
        print(cn)
        break
