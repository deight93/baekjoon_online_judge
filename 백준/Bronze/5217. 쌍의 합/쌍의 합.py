import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in input_list:
    temp = ""
    if i % 2 == 0:
        for j in range(1, i//2):
            if j == i//2-1:
                temp += " {} {}".format(j, i - j)
            else:
                temp += " {} {},".format(j, i - j)
    else:
        for j in range(1, i//2+1):
            if j == i//2:
                temp += " {} {}".format(j, i - j)
            else:
                temp += " {} {},".format(j, i - j)

    print("Pairs for {}:".format(i)+temp)