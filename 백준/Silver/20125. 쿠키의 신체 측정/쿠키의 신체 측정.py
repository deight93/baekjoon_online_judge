import sys

n = int(sys.stdin.readline().rstrip())
c = [sys.stdin.readline().rstrip() for _ in range(n)]
heart = [0, 0]
awl = [0, 0, 0, 0, 0]


for i, v in enumerate(c):
    if "*" in v:
        heart[0] = i + 2
        heart[1] = v.index("*")+1
        break

v_c = ["".join(i) for i in list(zip(*c))]
awl[2] = v_c[heart[1]-1].count("*")-2
for i in v_c[:heart[1]-1]:
    if 1 <= i.count("*") < 2:
        awl[0] += 1
    elif 2 <= i.count("*"):
        awl[0] += 1
        awl[3] += i.count("*")-1

for i in v_c[heart[1]:]:
    if 1 <= i.count("*") < 2:
        awl[1] += 1
    elif 2 <= i.count("*"):
        awl[1] += 1
        awl[4] += i.count("*")-1

print(" ".join([str(i) for i in heart]))
print(" ".join([str(i) for i in awl]))