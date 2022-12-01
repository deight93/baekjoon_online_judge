import sys

n = int(sys.stdin.readline())
join_list = [[j for j in input().split(" ")] for i in range(n)]
for k, v in enumerate(join_list):
    join_list[k].append(k)

join_list2 = sorted(join_list, key=lambda x: (int(x[0]), x[2]))

for i in join_list2:
    print("{} {}".format(i[0], i[1]))