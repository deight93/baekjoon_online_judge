input_list = [int(i) for i in input().split(" ")]

if input_list[0] > input_list[1]:
    print(">")
elif input_list[0] < input_list[1]:
    print("<")
elif input_list[0] == input_list[1]:
    print("==")