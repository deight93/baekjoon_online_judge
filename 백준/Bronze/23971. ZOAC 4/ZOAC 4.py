import sys

h, w, n, m = map(int, sys.stdin.readline().rstrip().split(" "))

x = 1 + (h-1)//(1+n)
y = 1 + (w-1)//(1+m)


print(x*y)


