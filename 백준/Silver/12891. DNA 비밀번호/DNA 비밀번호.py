import sys

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().rstrip()
a, c, g, t = map(int, sys.stdin.readline().split())

dna_cnt = {i:0 for i in ["A", "C", "G", "T"]}
cnt = 0

for i in dna[:p]:
    dna_cnt[i] += 1
if dna_cnt["A"] >= a and dna_cnt["C"] >= c and dna_cnt["G"] >= g and dna_cnt["T"] >= t:
    cnt += 1

for i in range(1, s-p+1):
    dna_cnt[dna[i-1]] -= 1
    dna_cnt[dna[i+p-1]] += 1

    if dna_cnt["A"] >= a and dna_cnt["C"] >= c and dna_cnt["G"] >= g and dna_cnt["T"] >= t:
        cnt += 1

print(cnt)