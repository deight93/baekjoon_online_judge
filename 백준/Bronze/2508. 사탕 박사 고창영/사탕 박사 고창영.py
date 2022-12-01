import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    b = sys.stdin.readline().rstrip()
    r, c = map(int, sys.stdin.readline().rstrip().split(" "))
    c_list = [sys.stdin.readline().rstrip() for __ in range(r)]
    rotated = ["".join(i) for i in list(zip(*c_list[::-1]))]

    c = 0
    for i in c_list:
        c += i.count(">o<")

    for i in rotated:
        c += i.count("^ov")

    print(c)
