import sys

n, x, k = map(int, sys.stdin.readline().rstrip().split(" "))

n_list = [i for i in range(1, n+1)]
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(k)]

for i in input_list:
    a = n_list[i[0]-1]
    b = n_list[i[1]-1]
    n_list[i[0]-1] = b
    n_list[i[1]-1] = a
print(n_list.index(x)+1)