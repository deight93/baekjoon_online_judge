import sys

n = int(sys.stdin.readline().rstrip())
m = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = 0
if len(m) > 1:
    temp = m[0]
    sorted_m = sorted(m[1:], reverse=True)
    t_m = sorted_m + [temp]
    while True:
        if max(t_m) == temp and t_m.count(temp) <= 1:
            break
        else:
            temp += 1
            sorted_m[0] -= 1
            sorted_m = sorted(sorted_m, reverse=True)
            t_m = sorted_m + [temp]
        cnt += 1
print(cnt)


