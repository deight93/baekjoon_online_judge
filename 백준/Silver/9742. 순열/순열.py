import sys
import itertools

s = sys.stdin.readlines()
for i in s:
    r, n = i.rstrip().split(" ")
    n = int(n)
    c = 0
    p = itertools.permutations(r)
    length = sum(1 for x in itertools.permutations(r))

    if n <= length and n != 0:
        for i in p:
            c += 1
            if c == n:
                print("{} {} = {}".format(r, n, "".join(i)))
                break
    else:
        print("{} {} = {}".format(r, n, "No permutation"))