import sys

s = int(sys.stdin.readline())

temp = 0
cnt = 0
for i in range(1, s+1):
    temp += i
    cnt += 1
    if s < temp:
        break

if cnt == 1:
    print(cnt)
else:
    print(cnt-1)