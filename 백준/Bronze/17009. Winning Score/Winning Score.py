
import sys

total = []
for _ in range(2):
    a = int(sys.stdin.readline().rstrip()) * 3
    b = int(sys.stdin.readline().rstrip()) * 2
    c = int(sys.stdin.readline().rstrip()) * 1
    total += [a+b+c]

if total[0] > total[1]:
    print('A')
elif total[1] > total[0]:
    print('B')
else:
    print('T')