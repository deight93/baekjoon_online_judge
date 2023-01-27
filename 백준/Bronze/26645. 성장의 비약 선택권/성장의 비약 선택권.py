import sys

n = int(sys.stdin.readline().rstrip())

if n < 206:
    print(1)
elif 206 <= n < 218:
    print(2)
elif 218 <= n < 229:
    print(3)
else:
    print(4)