import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    p = sys.stdin.readline().rstrip()
    if 9 >= len(p) >= 6:
        print("yes")
    else:
        print("no")
