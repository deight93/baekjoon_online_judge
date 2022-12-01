import sys

temp = [500, 100, 50, 10, 5, 1]
n = 1000-int(sys.stdin.readline())

cnt = 0
for i in temp:
    while True:
        if n >= i:
            n -= i
            cnt += 1
        else:
            break

print(cnt)