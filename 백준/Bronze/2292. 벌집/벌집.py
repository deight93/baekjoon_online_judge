c = int(input())

total = 1
cnt = 0
while True:
    cnt += 1
    if c == 1:
        print(cnt)
        break
    else:
        total += 6*cnt
        if total >= c:
            print(cnt+1)
            break