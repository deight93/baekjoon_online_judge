a, b, n = map(int, input().split())

t = a%b
for _ in range(n):
    t = t*10
    d = t//b
    t %= b
print(d)