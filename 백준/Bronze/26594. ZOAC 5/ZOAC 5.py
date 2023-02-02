import sys

k = sys.stdin.readline().rstrip()
c = 0
for i in k:
    if i == k[0]:
        c += 1
    else:
        break
print(c)