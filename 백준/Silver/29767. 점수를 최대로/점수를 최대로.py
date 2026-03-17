n, k = map(int, input().split())
sc = []
a = 0
for i in map(int, input().split()):
    a += i
    sc.append(a)
sc = sorted(sc, reverse=True)
print(sum(sc[:k]))