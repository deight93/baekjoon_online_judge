import sys

input_list = sys.stdin.readline().rstrip().upper().split(" ")
temp = [i.upper() for i in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']]

return_list = []
for k, i in enumerate(input_list):
    if k == 0:
        if i in temp:
            return_list += [i[0]]

    if i not in temp:
        return_list += [i[0]]

print("".join(return_list))