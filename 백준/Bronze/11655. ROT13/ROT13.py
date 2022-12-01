import sys

w = sys.stdin.readline().rstrip()
temp_num = [str(i) for i in range(0,10)]
temp = ""

for i in w:
    if i == " " or i in temp_num:
        temp += i
    else:
        if 65 <= ord(i) <= 90:
            if ord(i)+13 > 90:
                temp += chr(ord(i) + 13 - 90 + 64)
            else:
                temp += chr(ord(i)+13)

        if 97 <= ord(i) <= 122:
            if ord(i)+13 > 122:
                temp += chr(ord(i) + 13 - 122 + 96)
            else:
                temp += chr(ord(i)+13)

print(temp)