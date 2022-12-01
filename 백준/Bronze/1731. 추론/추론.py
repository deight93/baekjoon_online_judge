import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for i in range(n)]

for i in range(2):
    q_list = []
    for j in range(1, 3):
        if i == 0:
            q = input_list[j] - input_list[j-1]
        else:
            q = input_list[j]/input_list[j - 1]
        q_list += [q]

    if i == 0 and q_list[0]-q_list[1] == 0:
        print(input_list[-1]+q_list[-1])
        break
    if i == 1 and q_list[0]-q_list[1] == 0:
        print(int(input_list[-1]*q_list[-1]))
        break