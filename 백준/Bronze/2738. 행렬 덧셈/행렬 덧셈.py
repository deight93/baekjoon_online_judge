import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))


a = [[int(j) for j in sys.stdin.readline().split(" ")] for _ in range(n)]
b = [[int(j) for j in sys.stdin.readline().split(" ")] for _ in range(n)]

sum_a_b = []
for i in range(n):
    sum_a_b += [[str(x+y) for x, y in zip(a[i], b[i])]]
for i in sum_a_b:
    print(" ".join(i))