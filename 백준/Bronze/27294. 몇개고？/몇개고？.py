import sys

t, s = map(int, sys.stdin.readline().rstrip().split(" "))

if s == 1:
    print(280)
else:
    if t <= 11:
        print(280)
    elif 12 <= t <= 16:
        print(320)
    else:
        print(280)