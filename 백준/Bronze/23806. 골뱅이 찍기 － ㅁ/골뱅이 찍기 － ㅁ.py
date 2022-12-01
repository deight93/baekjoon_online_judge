import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n*5):
    if i < 1*n:
        print("@"*n*5)
    elif i >= n*4:
        print("@" * n * 5)
    else:
        print("@"*n + " "*n*3 + "@"*n )

