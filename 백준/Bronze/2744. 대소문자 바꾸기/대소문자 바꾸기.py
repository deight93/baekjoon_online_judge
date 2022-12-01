import sys

w = sys.stdin.readline().rstrip()

temp = ""
for i in w:
    if i.isupper():
        temp += i.lower()
    else:
        temp += i.upper()
print(temp)
