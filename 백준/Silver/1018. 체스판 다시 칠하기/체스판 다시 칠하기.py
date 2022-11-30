def change_char(char_list):
    temp = []
    for ii in ["W", "B"]:
        cnt = 0
        if ii == "W":
            ww = "W"
            bb = "B"
        else:
            ww = "B"
            bb = "W"

        for k1, i in enumerate(char_list):
            for k2, j in enumerate(i):
                if divmod(k1, 2)[1] == 0:
                    if divmod(k2, 2)[1] == 0:
                        if char_list[k1][k2] == ww:
                            pass
                        else:
                            char_list[k1][k2].replace(bb, ww)
                            cnt += 1
                    else:
                        if char_list[k1][k2] == bb:
                            pass
                        else:
                            char_list[k1][k2].replace(ww, bb)
                            cnt += 1
                else:
                    if divmod(k2, 2)[1] == 0:
                        if char_list[k1][k2] == bb:
                            pass
                        else:
                            char_list[k1][k2].replace(ww, bb)
                            cnt += 1
                    else:
                        if char_list[k1][k2] == ww:
                            pass
                        else:
                            char_list[k1][k2].replace(bb, ww)
                            cnt += 1
        temp += [cnt]

    return temp


input_list = [int(i) for i in input().split(" ")]
chase_list = [input() for i in range(input_list[0])]

temp = []
for i in range(input_list[0]-8+1):
    for j in range(input_list[1] - 8 + 1):

        k = [a[j:j+8] for a in chase_list[i:i + 8]]
        k2 = change_char(k)
        temp += k2

print(min(temp))