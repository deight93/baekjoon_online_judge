import sys

t = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split(" ") for i in range(t)]

for i in input_list:
    temp = ""
    for j in range(len(i[0])):
        if ord(i[0][j]) > ord(i[1][j]):
            temp += str(ord(i[1][j])+26-ord(i[0][j]))+" "
        else:
            temp += str(ord(i[1][j]) - ord(i[0][j]))+" "

    print("Distances: {}".format(temp))