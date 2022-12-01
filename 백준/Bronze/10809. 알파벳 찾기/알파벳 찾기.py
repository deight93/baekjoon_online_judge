char_list = [chr(i) for i in range(97, 123)]
input_char = input()

temp = ""
for i in char_list:
    ck = False
    for k, v in enumerate(input_char):
        if i == v:
            temp += str(k)+" "
            ck = True
            break

    if ck is False:
        temp += "-1 "

print(temp.rstrip())