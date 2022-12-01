import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
k_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

t = []
for k in k_list:
    for i in range(1, (n // k) + 1):
        t += [k*i]
print(sum(set(t)))
