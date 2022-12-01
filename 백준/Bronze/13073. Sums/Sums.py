
import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    s1 = n * (n + 1) // 2
    s2 = int((n * 2) * (n / 2))
    s3 = int((n * 2 + 2) * (n / 2))
    print(s1, s2, s3)