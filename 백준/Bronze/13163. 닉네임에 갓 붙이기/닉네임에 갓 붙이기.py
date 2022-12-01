import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    n_name = sys.stdin.readline().rstrip().split(" ")
    n_name[0] = "god"
    print("".join(n_name))
