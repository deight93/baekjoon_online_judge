while True:
    try:
        n, k = map(int,input().split())
        cnt = n
        temp = n
        while True:
            cnt += (temp // k)
            if temp < k:
                break
            else:
                temp = (temp // k) + (temp % k)
        print(cnt)
    except EOFError:
        break