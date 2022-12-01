import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n+2):
    if i == 0:
        temp = "" + "@"*(n+2)
    elif i == n+1:
        temp = "" + "@" * (n + 2)
    else:
        temp = "@"+" "*n+"@"
    print(temp)

