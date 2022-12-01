import sys

n = int(sys.stdin.readline().rstrip())

temp = [1]
temp2 = [1]

cnt = 0
while True:
    cnt += 1
    a = temp[cnt-1] + 4 + ((cnt-1)*4)
    temp.append(a)
    temp2.append(temp2[cnt-1]+a)
    if temp2[cnt-1] <= n < temp2[cnt-1]+a:
        print(cnt)
        break