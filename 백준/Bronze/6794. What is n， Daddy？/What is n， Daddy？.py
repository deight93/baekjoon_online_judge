import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
for i in range((n//2)+1):
    if i <= 5 and n-i <= 5:
        cnt += 1
print(cnt)

