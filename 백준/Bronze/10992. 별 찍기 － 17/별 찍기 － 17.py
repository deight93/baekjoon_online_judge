import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    c = " "*(n-i-1)
    a = "*"
    if i > 0:
        b = "*"
        if i == n-1:
            d = "*" * (2 * i - 1)
        else:
            d = " " * (2 * i - 1)
    else:
        d = " " * (2 * i - 1)
        b = ""
    print(c+a+d+b)
