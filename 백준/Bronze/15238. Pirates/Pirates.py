import sys

n = int(sys.stdin.readline().rstrip())
w = sys.stdin.readline().rstrip()

max_c = 0
c = "a"
for i in range(97, 123):
    if w.count(chr(i)) > max_c:
        max_c = w.count(chr(i))
        c = chr(i)

print(c, max_c)