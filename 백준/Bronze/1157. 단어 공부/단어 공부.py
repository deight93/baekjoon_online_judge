char_list = [chr(i) for i in range(97, 123)]
word = input().lower()

temp = []
for c in char_list:
    temp.append((word.count(c), c))

max_temp = max(temp)
cnt = 0
for j in temp:
    if j[0] == max_temp[0]:
        cnt += 1

if cnt == 1:
    print(max_temp[1].upper())
else:
    print("?")