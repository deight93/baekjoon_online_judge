import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    a = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    if a[2]-a[1] == a[1]-a[0]:
        d = a[1]-a[0]
        sn = (n*(2*a[0]+((n-1)*d)))/2
    else:
        r = a[1]/a[0]
        sn = a[0]*((r**n-1)/(r-1))

    print(int(sn))
