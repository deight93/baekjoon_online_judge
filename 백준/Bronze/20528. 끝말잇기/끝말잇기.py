import sys

n = int(sys.stdin.readline().rstrip())
si = sys.stdin.readline().rstrip().split(" ")
w = si[0][0]
ck = True

for i in si:
    if i[0] != w:
        ck = False
        break

if ck:
    print(1)
else:
    print(0)
