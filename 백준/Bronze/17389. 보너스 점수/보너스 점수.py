import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

b = 0
t = 0
for idx, v in enumerate(s):
    if v == "O":
        t += (idx+1)
        t += b
        b += 1
    else:
        b = 0

print(t)

