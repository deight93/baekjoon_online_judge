import sys

temp = []
n = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(4)]

for i in n:
    t = 0
    for j in range(4):
        t += i[j]
    temp += [t]
    temp += [sum(i)]

if len(set(temp)) == 1:
    print("magic")
else:
    print("not magic")


