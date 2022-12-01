import sys

n, fp, sp = sys.stdin.readline().rstrip().split(" ")
fp = list(fp)
sp = list(sp)
nfp = []
nsp = []

r = 0
s = 0

for i in range(int(n)):
    if fp[i] == sp[i]:
        r += 1
    else:
        nfp.append(fp[i])
        nsp.append(sp[i])

for i in nsp:
    if nfp.count(i) != 0:
        s += 1
        nfp.remove(i)

print(r, s)

