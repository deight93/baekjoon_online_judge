import sys

n = int(sys.stdin.readline().rstrip())
x = [int(sys.stdin.readline().rstrip()) for i in range(n)]

ab = []
for i in range(n):
    for j in range(i+1, n):
        ab.append(sum([min((x[i] - x[k]) ** 2, (x[j] - x[k]) ** 2) for k in range(n)]))

print(min(ab))


