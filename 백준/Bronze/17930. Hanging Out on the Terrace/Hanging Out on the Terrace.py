import sys

l, x = map(int, sys.stdin.readline().rstrip().split(" "))

cm = 0
o = 0
for i in range(x):
    w, p = sys.stdin.readline().rstrip().split(" ")
    if w == "enter":
        if cm + int(p) <= l:
            cm += int(p)
        else:
            o += 1
    else:
        cm -= int(p)

print(o)