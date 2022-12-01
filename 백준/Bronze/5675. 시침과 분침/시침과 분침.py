import sys

for n in sys.stdin:
    if int(n) % 6 == 0:
        print("Y")
    else:
        print("N")