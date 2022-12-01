
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]
p_list = [0 for _ in range(n)]

for _ in range(m):
    temp = []
    for i in input_list:
        max_c = max(i)
        temp += [max_c]
        i.remove(max_c)

    max_t = max(temp)
    for k, j in enumerate(temp):
        if j == max_t:
            p_list[k] += 1

max_p = max(p_list)
print(" ".join([str(k+1) for k, i in enumerate(p_list) if i == max_p]))