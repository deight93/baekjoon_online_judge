import sys

temp = []
while True:
    a = sys.stdin.readline().rstrip()
    if a == "END":
        break
    temp += [a]

for i in temp:
    print(i[::-1])