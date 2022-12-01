
while True:
    input_list = [int(i) for i in input().split(" ")]
    if input_list[0] == 0 and input_list[1] == 0:
        break
    else:
        print(input_list[0] + input_list[1])
