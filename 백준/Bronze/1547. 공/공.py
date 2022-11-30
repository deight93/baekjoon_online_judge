import sys

n = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(n)]

temp = [1, 2, 3]

for i in input_list:
    a = i[0]
    b = i[1]
    a_idx = temp.index(a)
    b_idx = temp.index(b)

    temp[a_idx] = b
    temp[b_idx] = a
print(temp[0])