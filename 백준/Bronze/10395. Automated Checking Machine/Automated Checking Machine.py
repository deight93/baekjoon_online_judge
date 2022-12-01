import sys

a = sys.stdin.readline().split(" ")
b = sys.stdin.readline().split(" ")

ck = True
for i in range(5):
    if a[i] == b[i]:
        ck = False
        break

if ck:
    print("Y")
else:
    print("N")

