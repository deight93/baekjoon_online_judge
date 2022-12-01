
import sys

while True:
    a_n, n = sys.stdin.readline().rstrip().split(" ")
    if a_n == "#" and n == "0":
        break
    n = int(n)
    while True:
        b, s = sys.stdin.readline().rstrip().split(" ")
        if b == "X" and s == "0":
            break
        else:
            s = int(s)
            if b == "B" and s+n <= 68:
                n += s

            if b == "C" and s <= n:
                n -= s
    print(a_n, n)