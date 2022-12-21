import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

cnt = 0
while True:
    if a >= 5 or b >= 5:
        break
    else:
        if cnt % 2 == 0:
            b += a
        else:
            a += b
        cnt += 1
if a > b:
    print("yj")
else:
    print("yt")

