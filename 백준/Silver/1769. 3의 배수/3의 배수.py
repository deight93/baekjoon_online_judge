
import sys

n = sys.stdin.readline().rstrip()
cnt = 0
while True:
    if len(n) == 1:
        print(cnt)
        if n in ['3', '6', '9']:
            print("YES")
        else:
            print("NO")
        break
    else:
        cnt += 1
        n = str(sum([int(i) for i in n]))