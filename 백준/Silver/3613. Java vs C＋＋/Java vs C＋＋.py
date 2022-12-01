
import sys

n = sys.stdin.readline().rstrip()

ck__ = False
ck_u = False
ck_l = False

for i in n:
    if i == "_":
        ck__ = True
    elif i.isupper():
        ck_u = True
    elif i.islower():
        ck_l = True

if ck__ is True and ck_u is False and ck_l is True and n[0] != "_" and n[-1] != "_" and n.find("__") == -1:
    for i in range(97, 123):
        n = n.replace("_"+chr(i), chr(i-32))
    print(n)
elif ck__ is False and ck_l is True and n[0].isupper() is False:
    for i in range(65, 91):
        n = n.replace(chr(i), "_" + chr(i + 32))
    print(n)
else:
    print("Error!")

