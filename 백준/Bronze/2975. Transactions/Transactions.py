import sys

while True:
    n = sys.stdin.readline().rstrip().split(" ")
    n1 = "".join(n[:-1]).replace(",", "")
    n2 = n[-1]
    if n1 == "0W" and n2 == "0":
        break
    else:
        if n1[-1] == "W":
            a = int(n1[:-1]) - int(n2)
            if a < -200:
                print("Not allowed")
            else:
                print(a)
        else:
            print(int(n1[:-1]) + int(n2))

