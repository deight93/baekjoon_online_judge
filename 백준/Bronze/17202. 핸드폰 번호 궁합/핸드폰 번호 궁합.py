import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

p = [int(j) for i in zip(a, b) for j in i]

while True:
    if len(p) == 2:
        print("".join([str(i) for i in p]))
        break
    else:
        temp = []
        for i in range(len(p)-1):
            temp += [int(str(p[i]+p[i+1])[-1])]
        p = temp

