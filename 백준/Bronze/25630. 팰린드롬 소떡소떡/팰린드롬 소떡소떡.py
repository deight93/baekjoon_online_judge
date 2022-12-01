import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

s1 = s[:n // 2]
if n % 2 == 0:
    s2 = s[n // 2:]
else:
    s2 = s[(n // 2)+1:]

c = 0
for i in range(n // 2):
    if s1[i] != s2[(n // 2)-(i+1)]:
        c += 1

print(c)

