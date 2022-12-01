import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n*5):
    if i < n:
        print("@@@" * n + " " * n + "@" * n)
    elif i >= (n*5)-n:
        print("@" * n + " " * n + "@@@" * n)
    else:
        print("@" * n + " " * n + "@" * n + " " * n + "@" * n)