while True:
    input_list = [int(i) for i in input().split(" ")]
    if sum(input_list) == 0:
        break

    c = max(input_list)
    input_list.remove(c)
    a = input_list[0]
    b = input_list[1]

    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")