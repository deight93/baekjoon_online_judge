import sys

n_a, n_b = map(int, sys.stdin.readline().rstrip().split(" "))
a = set(map(int, sys.stdin.readline().rstrip().split(" ")))
b = set(map(int, sys.stdin.readline().rstrip().split(" ")))

r = sorted(a-b)
if not r:
    print(0)
else:
    print(len(r))
    print(" ".join([str(i) for i in r]))
