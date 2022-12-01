import sys
import re

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = sys.stdin.readline().rstrip()
    temp = "{}{{2}}{}{{2}}{}{}{{2}}".format(n[0], n[-1], n[0], n[-1])
    if n.isalpha() and len(n) == 7 and len(set(n)) == 2 and re.match(temp, n):
        print(1)
    else:
        print(0)

