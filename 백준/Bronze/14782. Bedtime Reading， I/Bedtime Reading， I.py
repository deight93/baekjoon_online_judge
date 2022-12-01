import sys

n = int(sys.stdin.readline().rstrip())

temp = 0
for i in range(1, int(n/2)+1):
    if n%i == 0:
        temp += i

print(temp+n)
