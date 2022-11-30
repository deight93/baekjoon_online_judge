import sys

n = sorted(sys.stdin.readline().rstrip())

o_cnt = 0
temp_o = ""
for i in set(n):
    if n.count(i) % 2 == 1:
        o_cnt += 1
        temp_o = i
        n.pop(n.index(temp_o))
        n.append(i)

if o_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    temp = ["" for i in n]
    for k, i in enumerate(n):
        if k % 2 == 0:
            temp[k // 2] = i
        else:
            temp[-1 * ((k // 2) + 1)] = i
    print("".join(temp))