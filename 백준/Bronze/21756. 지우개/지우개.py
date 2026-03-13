n = int(input())

cnt = 0
while True:
    if int(n) == 1:
        break
    n /= 2
    cnt += 1

print(2**cnt)