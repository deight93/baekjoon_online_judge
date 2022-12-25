import sys

n = int(sys.stdin.readline().rstrip())

temp = []
for i, v in enumerate(str(bin(n))[2:][::-1]):
    if v == "1":
        temp.append(str(i))

print(" ".join(temp))

