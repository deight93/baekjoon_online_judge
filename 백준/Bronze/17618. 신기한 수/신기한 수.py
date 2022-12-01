import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
for i in range(1, n+1):
    t = 0
    for j in str(i):
        t += int(j)

    if i % t == 0:
        cnt += 1
print(cnt)

