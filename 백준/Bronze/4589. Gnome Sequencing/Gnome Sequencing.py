
import sys

n = int(sys.stdin.readline().rstrip())
n_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

print("Gnomes:")
for i in n_list:
    if i == sorted(i, reverse=True) or i == sorted(i, reverse=False):
        print("Ordered")
    else:
        print("Unordered")

