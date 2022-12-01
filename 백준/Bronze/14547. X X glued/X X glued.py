import sys

while True:
    n = sys.stdin.readline().strip()

    if n == "#":
        break
    else:
        a, b, c = n.split(" ")

        temp = []
        for i in range(3):
            if b[i] == b[i+1]:
                temp += ["{} {} glued".format(b[i], b[i])]

        if temp:
            print(" and ".join(set(temp)))

