import sys
n = int(sys.stdin.readline())

if n % 2 == 1:
    print(((n//2)+1)*((n//2)+2))
else:
    print(((n // 2) + 1) * ((n // 2) + 1))
