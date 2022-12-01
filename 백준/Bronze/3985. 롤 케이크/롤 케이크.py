import sys

l_list = [0 for _ in range(int(sys.stdin.readline().rstrip()))]

n = int(sys.stdin.readline().rstrip())

p_i = []
for i in range(n):
    p, k = map(int, sys.stdin.readline().rstrip().split(" "))
    p_i += [(i+1, k-p+1)]
    for j in range(p-1, k):
        if l_list[j] == 0:
            l_list[j] = i+1

print(max(p_i, key=lambda x:x[1])[0])
max_i = max([(i+1, l_list.count(i+1)) for i in range(n)], key=lambda x:x[1])
print(max_i[0])

