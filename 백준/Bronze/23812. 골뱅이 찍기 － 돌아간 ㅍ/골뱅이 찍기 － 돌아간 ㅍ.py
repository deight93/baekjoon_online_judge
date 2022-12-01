import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n*5):
    if i < n:
        print("@" * n + "   " * n + "@" * n)
    elif i >= (n*5)-n:
        print("@" * n + "   " * n + "@" * n)
    elif (n*3)-n <= i <= (n*3)-1:
        print("@" * n + "   " * n + "@" * n)
    else:
        print("@@@@@" * n)

