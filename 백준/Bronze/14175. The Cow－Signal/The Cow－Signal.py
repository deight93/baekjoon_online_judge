
import sys

m, n, k = map(int, sys.stdin.readline().rstrip().split(" "))

k_list = []
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    s_k = ""
    for i in s:
        s_k += i*k
    for i in range(k):
        k_list += [s_k]

for i in k_list:
    print(i)
