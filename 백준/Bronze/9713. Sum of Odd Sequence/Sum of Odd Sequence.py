import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    total = 0
    for i in range(1, a+1, 2):
        total += i
    print(total)