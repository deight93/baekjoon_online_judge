import sys

for i in range(int(sys.stdin.readline().rstrip())):
    abc = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    c = max(abc)
    abc.remove(c)
    a = abc[0]
    b = abc[1]
    if (a**2) + (b**2) == c**2:
        print("Case #{}: YES".format(i+1))
    else:
        print("Case #{}: NO".format(i + 1))


