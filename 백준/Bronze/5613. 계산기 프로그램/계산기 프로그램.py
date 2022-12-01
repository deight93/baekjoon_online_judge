import sys

temp = []
while True:
    a = sys.stdin.readline().rstrip()
    temp += [a]
    if a == "=":
        break

total = int(temp[0])
for i in range(0, len(temp), 2):
    if i == 0:
        pass
    else:
        if temp[i-1] == "+":
            total = int(total + int(temp[i]))
        elif temp[i-1] == "-":
            total = int(total - int(temp[i]))
        elif temp[i-1] == "*":
            total = int(total * int(temp[i]))
        elif temp[i-1] == "/":
            total = int(total / int(temp[i]))

print(total)