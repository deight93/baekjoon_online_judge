
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

cnt = 0
str_r = ""

while True:
    cnt += 1
    if cnt == 1:
        q = a // b
        r = a % b
        if r == 0:
            str_r = str_r + str(q)
        else:
            str_r = str_r + str(q) + "."
        a = int(str(r) + "0")
    else:
        q = a // b
        r = a % b
        str_r += str(q)
        a = int(str(r) + "0")

    if cnt > 1003:
        temp = str_r[:str_r.find(".")+1]+str_r[str_r.find(".")+1:str_r.find(".")+1001]
        print(temp.rstrip("0"))
        break
