
import sys

try:
    temp = ['P', 'K', 'H', 'T']
    c_dict = {}
    for i in temp:
        c_dict[i] = [i for i in range(1, 14)]

    n = sys.stdin.readline().rstrip()

    for i in range(0, len(n), 3):
        a = n[i:i+3]
        c_dict[a[0]].remove(int(a[1:]))

    b = [str(len(c_dict[i])) for i in temp]
    print(" ".join(b))
except ValueError:
    print("GRESKA")