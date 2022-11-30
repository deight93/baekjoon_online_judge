c = int(input())
input_list = [int(i) for i in input().split(" ")]

m = max(input_list)

total_n_n = 0
for i in input_list:
    n_n = i / m * 100
    total_n_n += n_n

print(total_n_n/c)
