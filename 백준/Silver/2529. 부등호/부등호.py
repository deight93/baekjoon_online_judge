import sys

n = int(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip().split(" ")
c = [False]*10
r_max, r_min = "", ""


def check(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


def solve(cnt, s):
    global r_max, r_min

    if cnt == n+1:
        if not len(r_min):
            r_min = s
        else:
            r_max = s
        return

    for i in range(10):
        if not c[i]:
            if cnt == 0 or check(s[-1], str(i), b[cnt-1]):
                c[i] = True
                solve(cnt+1, s+str(i))
                c[i] = False


solve(0, "")
print(r_max)
print(r_min)
