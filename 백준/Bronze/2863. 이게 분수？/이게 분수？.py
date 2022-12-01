
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
c, d = map(int, sys.stdin.readline().rstrip().split(" "))

temp = [a/c + b/d]

for i in range(3):
    if i == 0:
        temp.append(c/d + a/b)
    elif i == 1:
        temp.append(d/b + c/a)
    else:
        temp.append(b/a + d/c)

print(temp.index(max(temp)))