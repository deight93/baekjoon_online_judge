
while True:
    try:
        n, b, m = map(float, input().rstrip().split(" "))
        cnt = 0
        while True:
            cnt += 1
            a = n * (b / 100)
            n = n + a
            if n >= m:
                break
        print(cnt)
    except EOFError:
        break