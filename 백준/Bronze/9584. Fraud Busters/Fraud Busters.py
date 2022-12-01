import sys

dc = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

temp = []
for _ in range(n):
    sc = sys.stdin.readline().rstrip()

    k = list(zip(dc, sc))
    ck = True
    for i in k:
        if i[0] != "*":
            if i[0] != i[1]:
                ck = False
                break

    if ck is True:
        temp += [sc]

print(len(temp))
[print(i) for i in temp]
