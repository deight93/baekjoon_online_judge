
import sys

t = int(sys.stdin.readline().rstrip())
temp = "aeiouAEIOU"

for i in range(t):
    n = sys.stdin.readline().rstrip()
    if n[-1] in temp:
        print("Case #{}: {} is ruled by a queen.".format(i+1, n))
    else:
        if n[-1] == "y":
            print("Case #{}: {} is ruled by nobody.".format(i + 1, n))
        else:
            print("Case #{}: {} is ruled by a king.".format(i + 1, n))


