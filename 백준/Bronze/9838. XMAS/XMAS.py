import sys

n = int(sys.stdin.readline().rstrip())
k = [(i+1, int(sys.stdin.readline().rstrip())) for i in range(n)]
k = sorted(k, key=lambda x:x[1])
for i in k:
    print(i[0])

