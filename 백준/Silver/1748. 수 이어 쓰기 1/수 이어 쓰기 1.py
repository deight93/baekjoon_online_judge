import sys

n = sys.stdin.readline().rstrip()

temp = 9
r = 0
for i in range(1, len(n)+1):
    if i == len(n):
        r += ((int(n)-10**(i-1))+1)*i
    else:
        r += temp*(10**(i-1))*i
print(r)