import sys

s = sys.stdin.readline().rstrip()
temp = ""
k = ord
for i in s:
    if k(i)-3 < 65:
        temp += chr(k(i)+23)
    else:
        temp += chr(k(i)-3)
print(temp)