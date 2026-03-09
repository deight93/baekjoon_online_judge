n = int(input())

r = []
for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = map(int, (a, b, c))
    r.append([name, a, b, c])

r = sorted(r, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, a, b, c in r:
    print(name)