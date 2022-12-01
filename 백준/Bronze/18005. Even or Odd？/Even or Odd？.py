import sys

n = int(sys.stdin.readline().rstrip())
a = n % 4

if a == 1 or a == 3:
    print(0)
elif a == 2:
    print(1)
else:
    print(2)
