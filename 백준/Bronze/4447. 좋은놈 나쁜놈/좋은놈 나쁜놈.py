
import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().rstrip() for i in range(n)]

for i in input_list:
    if i.lower().count("g") > i.lower().count("b"):
        print(i+" is GOOD")
    elif i.lower().count("b") > i.lower().count("g"):
        print(i + " is A BADDY")
    else:
        print(i + " is NEUTRAL")
