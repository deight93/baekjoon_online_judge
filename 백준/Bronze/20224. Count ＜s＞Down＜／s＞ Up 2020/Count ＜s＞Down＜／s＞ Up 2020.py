import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        cnt = 0
        d = "".join(sys.stdin.readline().rstrip().split(" "))
        for i in range(n-3):
            if d[i:i+4] == "2020":
                cnt += 1
        print(cnt)