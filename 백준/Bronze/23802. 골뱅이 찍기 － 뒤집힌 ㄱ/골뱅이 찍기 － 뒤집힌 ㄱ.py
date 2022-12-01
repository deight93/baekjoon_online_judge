import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n*5):
    if i < n:
        print("@@@@@"*n)
    else:
        print("@"*n)

