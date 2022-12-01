
import sys

p = int(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline().rstrip())


if 50 >= p and 10 >= q:
    print("White")
else:
    if q > 30:
        print("Red")
    else:
        print("Yellow")

