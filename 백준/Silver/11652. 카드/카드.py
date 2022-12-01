import sys

n = int(sys.stdin.readline().rstrip())

input_dict = {}
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a in input_dict.keys():
        input_dict[a] += 1
    else:
        input_dict[a] = 1

print(sorted(input_dict.items(), key=lambda x: (-x[1], x[0]))[0][0])