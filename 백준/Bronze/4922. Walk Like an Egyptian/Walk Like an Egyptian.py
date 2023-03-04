import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        r = 1
        for i in range(1, n):
            r += 2*i
        print("{} => {}".format(n, r))