import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split(" "))

temp = [0]

for i in range(k+1):
    a = n-i
    b = m-(k-i)
    if a//2 >= 0 and b >= 0:
        temp += [min(a//2, b)]
print(max(temp))

