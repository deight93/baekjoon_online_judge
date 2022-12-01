import sys

t = int(sys.stdin.readline())

temp = [0, 1, 1, 1, 2, 2]
for j in range(6, 100 + 1):
    temp.append(temp[j - 5] + temp[j - 1])

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(temp[n])