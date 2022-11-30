import sys

n = int(sys.stdin.readline())

cnt = 665
temp = []
while True:
    cnt += 1
    if str(cnt).find("666") != -1:
        temp += [cnt]
    else:
        pass

    if len(temp) == n:
        break

print(temp[-1])
