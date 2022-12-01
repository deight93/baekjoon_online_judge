import sys

n = int(sys.stdin.readline().rstrip())

temp = {}
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(" ")

    if a in temp.keys():
        temp[a] += [b]
    else:
        temp[a] = [b]


cnt = 0
for k, v in temp.items():
    init_v = v[0]
    for i in range(1, len(v)):
        if init_v != v[i]:
            cnt += 1
            init_v = v[i]

print(cnt)
