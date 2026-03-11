from itertools import combinations

n, k = map(int, input().split())
hp = [list(map(int, input().split())) for _ in range(n)]

mr = []
for cp in combinations(hp, k):
    r = []
    for p in hp:
        if p in cp:
            continue

        r2 = []
        for c in cp:
            r2.append(abs(p[0]-c[0])+abs(p[1]-c[1]))
        r.append(min(r2))
    mr.append(max(r))
print(min(mr))