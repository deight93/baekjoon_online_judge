import sys

p = int(sys.stdin.readline().rstrip())

for i in range(p):
    k, n = map(int, sys.stdin.readline().rstrip().split(" "))

    s1 = n * (n + 1) // 2
    s2 = int((n * 2) * (n / 2))
    s3 = int((n * 2 + 2) * (n / 2))
    print(k, s1, s2, s3)
