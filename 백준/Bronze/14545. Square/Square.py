import sys

p = int(sys.stdin.readline().rstrip())
l_list = [int(sys.stdin.readline().rstrip()) for _ in range(p)]
max_l = max(l_list)

c = [0]
for i in range(1, max_l+1):
    c += [c[i-1]+i**2]

for i in l_list:
    print(c[i])

