import sys

temp = [0 for i in range(10000 + 1)]
temp[1] = 1
for i in range(2, int(10000**0.5)-2):
    for j in range(i * 2, 10001, i):
        temp[j] = 1

c = int(sys.stdin.readline())
for i in range(c):
    a = int(sys.stdin.readline())
    b = a // 2
    for j in range(b, 1, -1):
        if temp[a - j] == 0 and temp[j] == 0:
            print(j, a - j)
            break