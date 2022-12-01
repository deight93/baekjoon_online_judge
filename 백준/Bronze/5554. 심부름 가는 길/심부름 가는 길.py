import sys

total = sum([int(sys.stdin.readline().rstrip()) for _ in range(4)])
print(total // 60)
print(total % 60)