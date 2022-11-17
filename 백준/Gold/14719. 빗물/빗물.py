import sys

h, w = map(int, sys.stdin.readline().rstrip().split(" "))
b_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

t = 0
for i in range(w):
    if 0 < i < w-1:
        l = max(b_list[:i])
        r = max(b_list[i:])
        if min(l, r)-b_list[i] > 0:
            t += min(l, r)-b_list[i]
print(t)


