import sys

n = int(sys.stdin.readline().rstrip())
if n < 100:
    print(99)
else:
    min_cnt = [0, 0]
    for i in range(n-1, 1, -1):
        min_cnt[0] += 1
        if str(i)[-2:] == "99":
            min_cnt[1] = i
            break

    max_cnt = [0, 0]
    for i in range(n+1, n+100):
        max_cnt[0] += 1
        if str(i)[-2:] == "99":
            max_cnt[1] = i
            break

    if min_cnt[0] == max_cnt[0]:
        print(max_cnt[1])
    else:
        print(min(min_cnt, max_cnt, key=lambda x: x[0])[1])



