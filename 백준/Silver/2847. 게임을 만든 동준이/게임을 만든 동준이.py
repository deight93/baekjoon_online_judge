import sys

n = int(sys.stdin.readline().rstrip())
n_list = [int(sys.stdin.readline()) for _ in range(n)]
n_list.reverse()

t = 0
for i in range(1, n):
    if n_list[i-1] <= n_list[i]:
        dif = (n_list[i] - n_list[i-1] + 1)
        n_list[i] -= dif
        t += dif

print(t)
