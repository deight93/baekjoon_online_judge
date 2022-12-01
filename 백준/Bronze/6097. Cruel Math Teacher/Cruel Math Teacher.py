import sys

n, p = map(int, sys.stdin.readline().rstrip().split(" "))
r = str(n**p)
for i in range((len(r)//70)+1):
    print(r[i*70:(i+1)*70])

