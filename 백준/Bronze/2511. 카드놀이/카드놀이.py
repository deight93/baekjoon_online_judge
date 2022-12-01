import sys

a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b = list(map(int, sys.stdin.readline().rstrip().split(" ")))

s_a = 0
s_b = 0
e_w = 0
for i in range(10):
    if a[i] > b[i]:
        s_a += 3
        e_w = 1
    elif b[i] > a[i]:
        s_b += 3
        e_w = 2
    else:
        s_a += 1
        s_b += 1

print(s_a, s_b)
if s_a > s_b:
    print("A")
elif s_b > s_a:
    print("B")
else:
    if e_w == 1:
        print("A")
    elif e_w == 2:
        print("B")
    else:
        print("D")