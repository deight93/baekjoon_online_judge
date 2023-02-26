import sys

n = int(sys.stdin.readline().rstrip())
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

temp = ""
for i in list(zip(s1, s2)):
    a = sorted(i)
    if a == ['P', 'R']:
        temp += "P"
    elif a == ['P', 'S']:
        temp += "S"
    elif a == ['R', 'S']:
        temp += "R"
    else:
        if list(set(a))[0] == "R":
            temp += "P"
        elif list(set(a))[0] == "P":
            temp += "S"
        else:
            temp += "R"
print(temp)

