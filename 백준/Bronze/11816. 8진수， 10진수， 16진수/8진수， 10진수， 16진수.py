import sys

n = sys.stdin.readline().rstrip()

if n[0] == "0":
    if n[:2] == "0x":
        print(int(n[2:], 16))
    else:
        print(int(n[1:], 8))
else:
    print(n)