import sys

n, p = map(int, sys.stdin.readline().rstrip().split(" "))
cnt = 0
m = [[] for _ in range(n)]
for _ in range(n):
    line_num, fret = map(int, sys.stdin.readline().rstrip().split(" "))
    idx = line_num-1
    while True:
        if not m[idx]:
            cnt += 1
            m[idx].append(fret)
            break
        else:
            if m[idx][-1] < fret:
                m[idx].append(fret)
                cnt += 1
                break
            elif m[idx][-1] > fret:
                m[idx].pop()
                cnt += 1
            else:
                break
print(cnt)