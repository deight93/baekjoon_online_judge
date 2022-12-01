
import sys

n = int(sys.stdin.readline().rstrip())

s = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    d = (x ** 2 + y ** 2) ** 0.5

    temp = [190 < d]
    temp += [190 - (i * 20) < d <= 190 - ((i - 1) * 20) for i in range(1, 10)]
    temp += [d <= 10]
    s += temp.index(True)
print(s)


