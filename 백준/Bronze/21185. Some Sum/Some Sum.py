import sys

s = int(sys.stdin.readline().rstrip())

if s % 2 == 1:
    print("Either")
else:
    if s % 4 == 0:
        print("Even")
    else:
        print("Odd")