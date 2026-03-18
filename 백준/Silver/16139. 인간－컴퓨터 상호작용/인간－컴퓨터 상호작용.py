import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

prefix = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    prefix[idx][i+1] = prefix[idx][i] + 1

    for j in range(26):
        if j != idx:
            prefix[j][i+1] = prefix[j][i]

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)

    idx = ord(a) - ord('a')

    print(prefix[idx][r+1] - prefix[idx][l])