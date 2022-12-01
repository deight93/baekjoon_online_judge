import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if 1 <= n <= 500:
        h = [n]
        cnt = 1
        while True:
            if h[-1] == 1:
                break

            if h[cnt - 1] % 2 == 0:
                hn = h[cnt - 1] / 2
            else:
                hn = (3 * h[cnt - 1]) + 1
            h += [int(hn)]
            cnt += 1

        print(max(h))
    else:
        break

