import sys

n = int(sys.stdin.readline().rstrip())
t = list(map(int, sys.stdin.readline().rstrip().split(" ")))

maxt_list = []
for i in range(n-2):
    maxt = max([t[i], t[i+2]])
    maxt_list += [(i+1, maxt)]
min_max_t = min(maxt_list, key=lambda x: x[1])
print(min_max_t[0], min_max_t[1])