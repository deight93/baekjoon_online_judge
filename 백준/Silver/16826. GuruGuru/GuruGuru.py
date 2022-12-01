import sys

n = sys.stdin.readline().rstrip()

t = 0
cnt = 0
for i in n:
    if i == 'R':
        t += 90
    else:
        t -= 90

    if t == 360:
        t = 0
        cnt += 1

    if t == -360:
        t = 0

print(cnt)
