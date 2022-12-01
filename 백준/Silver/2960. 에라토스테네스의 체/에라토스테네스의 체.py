import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
temp = [i for i in range(2, n+1)]
temp_k = 0
r_list = []
while True:
    if k <= temp_k:
        break
    p = min(temp)
    len_temp = len(temp)
    for i in range(p, max(temp)+1, p):
        if i in temp:
            temp_k += 1
            temp.remove(i)
            r_list += [i]

print(r_list[k-1])