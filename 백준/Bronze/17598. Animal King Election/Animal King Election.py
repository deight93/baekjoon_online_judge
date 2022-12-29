import sys

t = 0
l = 0
for _ in range(9):
    a = sys.stdin.readline().rstrip()
    if a == "Tiger":
        t += 1
    else:
        l += 1

if t > l:
    print("Tiger")
else:
    print("Lion")


