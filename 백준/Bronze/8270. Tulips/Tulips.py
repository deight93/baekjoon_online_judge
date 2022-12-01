import sys

n = int(sys.stdin.readline().rstrip())
t_c = len(set(list(map(int, sys.stdin.readline().rstrip().split(" ")))))
print(15000-t_c)

