import sys

n = int(sys.stdin.readline().rstrip())
nl = [sys.stdin.readline().rstrip() for _ in range(n)]

if "anj" in nl:
    print("뭐야;")
else:
    print("뭐야?")

