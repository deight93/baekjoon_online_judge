import sys

n = sys.stdin.readline().rstrip()
p = n.replace("XXXX", "AAAA")
p = p.replace("XX", "BB")
if "X" in p:
    print(-1)
else:
    print(p)