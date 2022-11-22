import sys

m = int(sys.stdin.readline().rstrip())
s = set()

for i in range(m):
    l = sys.stdin.readline().rstrip()
    if l == "all":
        s = set([i for i in range(1, 21)])
    elif l == "empty":
        s = set()
    else:
        c, x = l.split(" ")
        x = int(x)
        if c == "add":
            s.add(x)
        elif c == "remove":
            s.discard(x)
        elif c == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)

