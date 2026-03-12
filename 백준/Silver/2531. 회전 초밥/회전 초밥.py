n, d, k, c = map(int, input().split())
chobabs = [int(input()) for _ in range(n)]
chobabs += chobabs[:k]

ml = 0
for i in range(n):
    pc = set(chobabs[i:i+k])
    lpc = len(pc)
    if c not in pc:
        lpc += 1
    ml = max(ml, lpc)

print(ml)