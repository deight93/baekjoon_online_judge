n = int(input())
times = [list(map(int, input().split(" "))) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

et = times[0][1]
cnt = 1
for t in times[1:]:
    st = t[0]
    if st < et:
        continue
    cnt += 1
    et = t[1]

print(cnt)