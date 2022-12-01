import sys

while True:
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    s = [0, 0]
    if a == "E" and b == "E":
        break
    else:
        for i in range(len(a)):
            if a[i] == 'R':
                if b[i] == 'P':
                    s[1] += 1
                if b[i] == 'S':
                    s[0] += 1

            if a[i] == 'P':
                if b[i] == 'S':
                    s[1] += 1
                if b[i] == 'R':
                    s[0] += 1

            if a[i] == 'S':
                if b[i] == 'R':
                    s[1] += 1
                if b[i] == 'P':
                    s[0] += 1
    print("P1: {}".format(s[0]))
    print("P2: {}".format(s[1]))

