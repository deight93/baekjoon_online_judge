
import sys

input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(2)]

for i in input_list:
    a = i[0]
    for j in range(1, int(len(i))):
        i[j] += a
        a = i[j]

a2 = 'No'
for i in range(9):
    if i == 0:
        if input_list[0][i] != 0:
            a2 = "Yes"
            break
    else:
        if input_list[0][i] > input_list[1][i-1]:
            a2 = "Yes"
            break
print(a2)