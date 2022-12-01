import sys

c = sys.stdin.readline().rstrip()
h = c.count(":-)")
s = c.count(":-(")

if h == 0 and s == 0:
    print("none")
else:
    if h > s:
        print("happy")
    elif h == s:
        print("unsure")
    else:
        print("sad")