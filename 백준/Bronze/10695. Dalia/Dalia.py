import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n, r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split(" "))
    p_p = [(r1-1, c1+2), (r1-1, c1-2), (r1+1, c1+2), (r1+1, c1-2), (r1-2, c1+1),
           (r1-2, c1-1), (r1+2, c1+1), (r1+2, c1-1)]
    if r2 <= n and c2 <= n:
        ck = False
        for j in p_p:
            if (r2, c2) == j:
                ck = True
                break
        if ck:
            print("Case {}: YES".format(i + 1))
        else:
            print("Case {}: NO".format(i + 1))
    else:
        print("Case {}: NO".format(i + 1))




