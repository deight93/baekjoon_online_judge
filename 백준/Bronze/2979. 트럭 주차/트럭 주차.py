import sys

a_b_c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(3)]
temp_a, temp_d = zip(*input_list)

temp = [0 for i in range(max(temp_d))]

for i in input_list:
    for j in range(i[0], i[1]):
        temp[j] += 1

p = 0
for i in temp:
    if i != 0:
        p += i*a_b_c[i-1]
print(p)