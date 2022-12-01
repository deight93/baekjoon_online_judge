import sys

temp = {}
t = 0
a = 0

while True:
    log = sys.stdin.readline().rstrip()
    if log == "-1":
        break
    else:
        m, n, r = log.split(" ")
        if r == "right":
            t += 1
            a += int(m)
            if n in temp.keys():
                a += 20*temp[n]
        else:
            if n in temp.keys():
                temp[n] += 1
            else:
                temp[n] = 1

print(t, a)
