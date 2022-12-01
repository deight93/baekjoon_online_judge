
import sys

d, k = map(int, sys.stdin.readline().rstrip().split(" "))

a = [1, 0]
b = [0, 1]

for i in range(2, d):
    a.append(a[i - 1] + a[i - 2])
    b.append(b[i - 1] + b[i - 2])

temp = 0
while True:
    temp += 1
    x = a[-1] * temp
    y = k - x
    if y % b[-1] == 0:
        print(temp)
        print(y // b[-1])
        break