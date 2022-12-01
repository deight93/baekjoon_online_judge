import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    c = " "*(n-i-1)
    a = "*"
    b = " *"*i
    print(c+a+b)