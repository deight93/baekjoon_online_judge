c = int(input())

for i in range(c):
    input_list = [i for i in input().split(" ")]

    temp = ""
    for k in input_list[1]:
        for j in range(int(input_list[0])):
            temp += k
    print(temp)