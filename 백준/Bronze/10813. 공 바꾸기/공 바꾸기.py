import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    a = n_list[i - 1]
    b = n_list[j - 1]
    n_list[i - 1] = b
    n_list[j - 1] = a

print(" ".join([str(i) for i in n_list]))