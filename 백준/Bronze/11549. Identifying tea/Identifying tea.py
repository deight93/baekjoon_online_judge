import sys

t = int(sys.stdin.readline().rstrip())
t_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
print(t_list.count(t))