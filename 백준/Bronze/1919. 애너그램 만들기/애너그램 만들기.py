
import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
a_l = len(a)
b_l = len(b)

for i in a:
    if b.count(i) != -1:
        b = b.replace(i, "", 1)

print(len(b) + len(a) - (b_l - len(b)))