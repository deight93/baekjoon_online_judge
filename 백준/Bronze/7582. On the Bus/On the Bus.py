
import sys

while True:
    n, z = sys.stdin.readline().rstrip().split(" ")
    if n == "#" and z == "0":
        break
    else:
        z = int(z)
        p = int(sys.stdin.readline().rstrip())
        s = int(sys.stdin.readline().rstrip())
        for _ in range(s):
            a, b = map(int, sys.stdin.readline().rstrip().split(" "))
            p -= a
            if b >= z-p:
                p = z
            else:
                p += b
        print(n, p)
