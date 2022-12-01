input_list = [int(i) for i in input().split(" ")]
input_list2 = [int(i) for i in input().split(" ")]

k = ""
for i in input_list2:
    if i < input_list[1]:
        k += "{} ".format(str(i))

print(k.rstrip())