import itertools

n_m = [int(i) for i in input().split(" ")]
input_list = [int(i) for i in input().split(" ")]

k = [sum(i) for i in list(itertools.permutations(input_list, 3))]

k2 = [i for i in k if i <= n_m[1]]
print(max(k2))