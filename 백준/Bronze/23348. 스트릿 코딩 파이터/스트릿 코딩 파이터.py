import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
n = int(sys.stdin.readline().rstrip())

s = []
for i in range(n):
    temp = 0
    for j in range(3):
        ai, bi, ci = map(int, sys.stdin.readline().rstrip().split(" "))
        temp += a * ai
        temp += b * bi
        temp += c * ci
    s += [temp]
print(max(s))

