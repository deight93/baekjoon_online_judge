import sys

n = sys.stdin.readline().rstrip()
len_n = len(n)//2
a = n[:len_n]
b = n[len_n:]
print(a, b)

