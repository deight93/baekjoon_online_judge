s = input()
n = int(input())
for _ in range(n):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(s[l:r+1].count(a))
