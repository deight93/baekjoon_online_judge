import sys

y = {"2", "0", "1", "8"}
n = sys.stdin.readline().rstrip()
set_n = set(n)

if set_n - y:
    print(0)
else:
    if y - set_n:
        print(1)
    else:
        if len(set([n.count(i) for i in y])) != 1:
            print(2)
        else:
            print(8)
