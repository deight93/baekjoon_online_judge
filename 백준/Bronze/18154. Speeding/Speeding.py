import sys

n = int(sys.stdin.readline().rstrip())
i_t, i_d = map(int, sys.stdin.readline().rstrip().split(" "))
a = 0

for i in range(n-1):
    t, d = map(int, sys.stdin.readline().rstrip().split(" "))
    a = max(a, (d-i_d)//(t-i_t))
    i_d = d
    i_t = t
print(a)

