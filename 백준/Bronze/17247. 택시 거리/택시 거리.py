import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
t_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

temp = []
for ki, i in enumerate(t_list):
    for kj, j in enumerate(i):
        if j == 1:
            temp += [(ki, kj)]

print(abs((temp[0][0]-temp[1][0]))+abs((temp[0][1]-temp[1][1])))

