import sys

t = int(sys.stdin.readline().rstrip())
n = map(int, sys.stdin.readline().rstrip().split(" "))

total = 0
cnt = 0
for i in n:
    if i != -1:
        total += i
        cnt += 1

print(total/cnt)