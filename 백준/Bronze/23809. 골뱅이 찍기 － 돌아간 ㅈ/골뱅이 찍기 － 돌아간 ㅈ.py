import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n*5):
    if i // n == 0:
        print("@" * n + " " * n * 3 + "@" * n)
    elif i // n == 1:
        print("@" * n + " " * n * 2 + "@" * n)
    elif i // n == 2:
        print("@" * n * 3)
    elif i // n == 3:
        print("@" * n + " " * n * 2 + "@" * n)
    else:
        print("@" * n + " " * n * 3 + "@" * n)
