
import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = [i for i in range(1, n+1)]

s_n = k-1
temp = []
while len(n_list):
    if s_n >= len(n_list):
        s_n = s_n % len(n_list)
    else:
        temp += [str(n_list.pop(s_n))]
        s_n += (k - 1)
print("<"+", ".join(temp)+">")