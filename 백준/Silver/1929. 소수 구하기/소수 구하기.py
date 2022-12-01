input_list = [int(i) for i in input().split(" ")]

for i in range(input_list[0], input_list[1]+1):
    ck = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            ck = False
            break

    if ck is True:
        if i != 1:
            print(i)