while True:
    try:
        input_list = [int(i) for i in input().split(" ")]
        print(input_list[0] + input_list[1])
    except Exception as ex:
        break