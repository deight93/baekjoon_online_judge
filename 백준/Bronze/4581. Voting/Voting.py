
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == "#":
        break
    else:
        if n.count("A") >= len(n)/2:
            print("need quorum")
        else:
            if n.count("Y") == n.count("N"):
                print("tie")
            elif n.count("Y") > n.count("N"):
                print("yes")
            elif n.count("Y") < n.count("N"):
                print("no")
