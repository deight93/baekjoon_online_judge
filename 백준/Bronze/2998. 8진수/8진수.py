import sys

temp = {"000": "0", "001": "1", "010": "2", "011": "3", "100": "4", "101": "5", "110": "6", "111": "7" }

b = sys.stdin.readline().rstrip()
if len(b) % 3 != 0:
    a = "0"*(3-(len(b)%3))
    b = a+b

s_l = []
n = 3
for index in range(0, len(b), n):
    s_l.append(b[index:index + n])

p = ""
for i in s_l:
    p += temp[i]
print(p)