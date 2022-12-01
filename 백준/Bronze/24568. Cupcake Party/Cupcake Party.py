import sys

a = int(sys.stdin.readline().rstrip()) * 8
b = int(sys.stdin.readline().rstrip()) * 3

if a+b > 28:
    print(a+b-28)
else:
    print(0)