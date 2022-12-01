import sys

n = int(sys.stdin.readline().rstrip())
l_a, r_a = sys.stdin.readline().rstrip().split(" -1 ")
print(min(map(int, l_a.split(" "))) + min(map(int, r_a.split(" "))))
