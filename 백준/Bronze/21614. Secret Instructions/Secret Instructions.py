import sys


ck = True
while True:
    s = sys.stdin.readline().rstrip()
    if s == "99999":
        break
    else:
        if sum([int(s[0]), int(s[1])]) == 0:
            print(ck, s[2:])
        else:
            if sum([int(s[0]), int(s[1])]) % 2 == 0:
                ck = "right"
                print("right", s[2:])
            else:
                ck = "left"
                print("left", s[2:])