import sys


while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    else:
        p = 0
        t = 0
        for _ in range(n):
            a, b = map(int, sys.stdin.readline().rstrip().split(" "))
            t += a*(b-p)
            p = b
        print("{} miles".format(t))

