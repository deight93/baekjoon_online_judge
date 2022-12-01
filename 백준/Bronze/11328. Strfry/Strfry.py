
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(" ")

    if len(a) != len(b):
        print("Impossible")
    else:
        set_a = set(a)

        temp = {}
        for i in set_a:
            temp[i] = a.count(i)

        ck = True
        for k, v in temp.items():
            if b.count(k) != v:
                ck = False
                break

        if ck:
            print("Possible")
        else:
            print("Impossible")
