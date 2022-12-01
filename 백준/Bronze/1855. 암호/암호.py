import sys

n = int(sys.stdin.readline().rstrip())
k = sys.stdin.readline().rstrip()

r_list = []
for i in range(1, len(k)//n+1):
    if i % 2 == 0:
        temp = k[(i-1) * n: i * n]
        temp = temp[::-1]
    else:
        temp = k[(i-1) * n: i * n]
    r_list += [temp]

r = ""
for i in zip(*r_list):
    r += "".join(i)
print(r)