
import sys

while True:
    n = int(sys.stdin.readline().rstrip())

    s = [0, 0]
    if n == 0:
        break
    else:
        a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        b = list(map(int, sys.stdin.readline().rstrip().split(" ")))

        for i in range(n):
            if a[i] != b[i]:
                if abs(a[i]-b[i]) > 1:
                    if a[i] > b[i]:
                        s[0] += a[i]
                    else:
                        s[1] += b[i]
                else:
                    if a[i] < b[i]:
                        if a[i] == 1:
                            s[0] += 6
                        else:
                            s[0] += (a[i]+b[i])
                    else:
                        if b[i] == 1:
                            s[1] += 6
                        else:
                            s[1] += (a[i]+b[i])

    print("A has {} points. B has {} points.".format(s[0], s[1]))
    print()
