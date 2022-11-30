import sys

input_list = [sys.stdin.readline().rstrip() for _ in range(8)]

cnt = 0
for k, v in enumerate(input_list):
    if k % 2 == 0:
        for j in v[::2]:
            if j == "F":
                cnt += 1
    else:
        for j in v[1::2]:
            if j == "F":
                cnt += 1

print(cnt)