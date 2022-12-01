import sys

init_input = sys.stdin.readline().rstrip().split(" ")
max_len = max(len(init_input[0]), len(init_input[1]))
a = init_input[0].zfill(max_len)
b = init_input[1].zfill(max_len)

temp = ""
for i in range(len(a)):
    temp += str(int(a[i]) + int(b[i]))
print(temp)
