import sys

w = sys.stdin.readline().rstrip()
c = "CAMBRIDGE"

temp = ""
for i in w:
    if i in c:
        pass
    else:
        temp += i
print(temp)
