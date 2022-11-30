import sys

n = int(sys.stdin.readline())

temp = [0, 0]
for i in range(2, n + 1):
    temp.append(temp[i - 1] + 1)
    if i % 3 == 0:
        temp[i] = min(temp[i], temp[i // 3] + 1)
    if i % 2 == 0:
        temp[i] = min(temp[i], temp[i // 2] + 1)
print(temp[n])