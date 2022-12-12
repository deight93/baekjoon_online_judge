import sys


w = sys.stdin.readline().rstrip()

s = 0
s_total = 0
for i, v in enumerate(w[:-1]):
    if v == "(" and w[i+1] == ")":
        s_total += s
    elif v == "(" and w[i+1] == "(":
        s += 1
    elif v == ")" and w[i+1] == "(":
        pass
    elif v == ")" and w[i + 1] == ")":
        s -= 1
        s_total += 1


print(s_total)

