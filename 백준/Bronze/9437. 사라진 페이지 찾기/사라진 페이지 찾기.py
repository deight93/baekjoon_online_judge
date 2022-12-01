
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == "0":
        break
    else:
        n, p = map(int, n.split(" "))
        for i in range(1, (n//4)+1):
            temp = [(i*2)-1, i*2, n-(i*2)+1, n-(i*2)+2]
            if p in temp:
                temp.remove(p)
                break
        print(" ".join([str(i) for i in temp]))