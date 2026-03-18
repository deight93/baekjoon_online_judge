s = input().strip()
n = int(input())

prefix = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    for j in range(26):
        prefix[j][i+1] = prefix[j][i]
    prefix[idx][i+1] += 1

for _ in range(n):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    idx = ord(a) - ord('a')

    print(prefix[idx][r+1] - prefix[idx][l])