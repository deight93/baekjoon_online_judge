import sys
from itertools import groupby

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    s2 = ["".join(grp) for num, grp in groupby(s)]
    s3 = [(str(len(i)), i[0]) for i in s2]
    print(" ".join([" ".join(i) for i in s3]))


