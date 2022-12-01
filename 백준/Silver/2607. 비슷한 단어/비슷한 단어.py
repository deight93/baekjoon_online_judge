
import sys

t = int(sys.stdin.readline().rstrip())
n = sys.stdin.readline().rstrip()

cnt = 0
for _ in range(t-1):
    n2 = sys.stdin.readline().rstrip()
    n_c = n
    if len(n2) == len(n)-1:
        for i in n2:
            ind = n.find(i)
            if ind != -1:
                n_c = n_c.replace(i, "", 1)

        if len(n_c) == 1:
            cnt += 1

    elif len(n2) == len(n):
        for i in n2:
            ind = n.find(i)
            if ind != -1:
                n_c = n_c.replace(i, "", 1)
        if len(n_c) == 0 or len(n_c) == 1:
            cnt += 1

    elif len(n2) == len(n)+1:
        for i in n2:
            ind = n.find(i)
            if ind != -1:
                n_c = n_c.replace(i, "", 1)

        if len(n_c) == 0:
            cnt += 1
    else:
        pass

print(cnt)