import sys
temp = []
while True:
    s = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if s[0] == 0 and s[1] == 0 and s[2] == 0:
        break
    temp += [s]

for s in temp:
    s = sorted(s, reverse=True)
    if s[0] < s[1] + s[2]:
        if len(set(s)) == 1:
            print("Equilateral")
        elif len(set(s)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")