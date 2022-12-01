import sys

n = int(sys.stdin.readline().rstrip())

total = 0
for i in range(2, n+2):
    if i == 2:
        a = 0
    else:
        a = ((i-2)*2)+1
    total += (i*5)-5-a
print(total%45678)