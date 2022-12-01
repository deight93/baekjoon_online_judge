import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == "EOI":
        break
    else:
        if s.lower().find("nemo") != -1:
            print("Found")
        else:
            print("Missing")