
import sys
import itertools

n = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

t = []
for k, i in enumerate(input_list):
    temp = sorted(i)
    t.append((k, int(max([str(sum(i))[-1] for i in set(itertools.combinations(temp, 3))]))))

print(max(t, key=lambda x: (x[1], x[0]))[0]+1)
