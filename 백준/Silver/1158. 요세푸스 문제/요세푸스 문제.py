
import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
n_list = [i for i in range(1, n+1)]

seq_num = k-1
temp = []
while len(n_list):
    if seq_num >= len(n_list):
        seq_num = seq_num % len(n_list)
    else:
        temp.append(str(n_list.pop(seq_num)))
        seq_num += (k - 1)
print("<"+", ".join(temp)+">")