import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))
t = a

while True:
    if a // b == 0:
        break
    else:
        t += a//b
        a = a//b
print(t)

