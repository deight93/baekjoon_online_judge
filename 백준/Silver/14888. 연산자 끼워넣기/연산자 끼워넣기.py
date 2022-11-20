from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))

temp_list = []
for k, i in enumerate(op_list):
    if k == 0:
        for j in range(i):
            temp_list += ["+"]
    elif k == 1:
        for j in range(i):
            temp_list += ["-"]
    elif k == 2:
        for j in range(i):
            temp_list += ["*"]
    elif k == 3:
        for j in range(i):
            temp_list += ["/"]

cal_list = list(set(permutations(temp_list, n-1)))

return_list = []
for op in cal_list:
    return_val = num_list[0]
    for k, v in enumerate(op):
        if v == "+":
            return_val += num_list[k+1]
        elif v == "-":
            return_val -= num_list[k + 1]

        elif v == "*":
            return_val *= num_list[k + 1]
        elif v == "/":
            return_val = int(return_val / num_list[k+1])
    return_list += [return_val]

print(max(return_list))
print(min(return_list))