import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split(" "))

p_o = m
p_x = n-m
b_o = k
b_x = n-k
print(min(p_o, b_o)+min(p_x, b_x))
