import sys

n = int(sys.stdin.readline().rstrip())
n_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]
stack = []
p = []
input_num = 1
ck = True

for i in n_list:
    while True:
        if input_num > i:
            break
        else:
            stack.append(input_num)
            p.append("+")
            input_num += 1

    if stack[-1] == i:
        stack.pop()
        p.append("-")
    else:
        print("NO")
        ck = False
        break

if ck:
    for i in p:
        print(i)




