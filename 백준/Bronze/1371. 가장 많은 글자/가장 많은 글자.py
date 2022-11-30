import sys

temp = sys.stdin.read()
temp = temp.replace(" ", "")
temp = temp.replace("\n", "")

char_list = [chr(i) for i in range(97, 123)]

temp2 = []
for i in char_list:
    temp2 += [temp.count(i)]

a = ""
for k, j in enumerate(temp2):
    if j == max(temp2):
        a += char_list[k]

print(a)
