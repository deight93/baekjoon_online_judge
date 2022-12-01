import sys

temp = """*** *** *** *** ***
*.* *.* *.. *.* *..
*** *** *.. *.* ***
*.* *.* *.. *.* *..
*.* *** *** *** ***""".split("\n")
temp = [i.split(" ") for i in temp]
f_t = list(zip(*temp))

l1 = int(sys.stdin.readline().rstrip())
l2 = sys.stdin.readline().rstrip()

p_l = []
for k, i in enumerate(l2):
    if k == 0:
        for j in f_t[ord(i)-65]:
            p_l += [j]
    else:
        for k2, j in enumerate(f_t[ord(i) - 65]):
            p_l[k2] += j

for i in p_l:
    print(i)

