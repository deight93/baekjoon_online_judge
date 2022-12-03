import sys

r, b = map(int, sys.stdin.readline().rstrip().split(" "))
s_rb = r+b

for l in range(1, r):
    if s_rb % l == 0:
        if b == (l-2)*((s_rb/l)-2):
            w = s_rb/l
            break

print(int(w), l)
