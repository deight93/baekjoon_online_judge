import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split(" "))

for x in range(-999, 1000):
    if e != 0:
        if c == (a*x)+(b*(((f-(d*x))/e))):
            for y in range(-999, 1000):
                if ((a + d) * x) + ((b + e) * y) == c + f:
                    print(x, y)
                    break
            break
    elif b != 0:
        if f == (d*x)+(e*(((c-(a*x))/b))):
            for y in range(-999, 1000):
                if ((a + d) * x) + ((b + e) * y) == c + f:
                    print(x, y)
                    break
            break