import sys

w = sys.stdin.readline().rstrip()
cnt = 0
for i, v in enumerate(w):
    if i % 3 == 0:
        if v != "P":
            cnt += 1
    elif i % 3 == 1:
        if v != "E":
            cnt += 1
    else:
        if v != "R":
            cnt += 1
print(cnt)


