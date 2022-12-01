import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

for i in range(n):
    if s[i:].count("s") == s[i:].count("t"):
        print(s[i:])
        break
