
import sys

while True:
    temp = sys.stdin.readline().rstrip()
    if temp == "*":
        break

    s = len(set([i[0] for i in temp.lower().split(" ")]))
    if s == 1:
        print("Y")
    else:
        print("N")