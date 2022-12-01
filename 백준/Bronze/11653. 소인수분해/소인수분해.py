p_n = int(input())
temp = []

for i in range(2, int(p_n**0.5)+1):
    if p_n % i == 0:
        temp += [i]
        temp += [int(p_n/i)]

temp = sorted(list(set(temp)))

if not temp:
    temp += [p_n]

temp_list = []
ck = False
if p_n != 1:
    while True:
        if ck is True:
            break
        else:
            for i in temp:
                div_mod = divmod(p_n, i)
                if div_mod[1] == 0:
                    temp_list += [i]
                    p_n = div_mod[0]

                    if div_mod[0] == 1:
                        ck = True
                        break
                    else:
                        break

for i in temp_list:
    print(i)