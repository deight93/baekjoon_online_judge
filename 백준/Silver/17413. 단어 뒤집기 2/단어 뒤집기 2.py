import sys

s = sys.stdin.readline().rstrip()
p_s = ""
w = ""
ck_tag = False

for k, i in enumerate(s):
    if ck_tag:
        w += i
        if i == ">":
            ck_tag = False
            p_s += w
            w = ""
    else:
        if i == "<":
            ck_tag = True
            p_s += "".join(list(w)[::-1])
            w = ""
            w += i
        elif i == " ":
            p_s += "".join(list(w)[::-1])
            p_s += i
            w = ""
        elif k == len(s)-1:
            p_s += i
            p_s += "".join(list(w)[::-1])
        else:
            w += i
print(p_s)

