

import sys


while True:
    n, a, w = sys.stdin.readline().rstrip().split(" ")
    if n == "#" and a == "0" and w == "0":
        break
    else:
        if int(a) > 17 or int(w) >= 80:
            c = "Senior"
        else:
            c = "Junior"

        print(n, c)


