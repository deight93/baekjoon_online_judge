import sys

input_list = [sys.stdin.readline().rstrip() for i in range(5)]

p = ""
ck = True
for k, i in enumerate(input_list):
    if i.find("FBI") != -1:
        p += str(k+1)+" "
        ck = False

if ck is True:
    print("HE GOT AWAY!")
else:
    print(p)
