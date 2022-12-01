import sys
import datetime

cnt = 0
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    else:
        cnt += 1
        temp = [0] * 12
        for _ in range(n):
            d, m, y = map(int, sys.stdin.readline().rstrip().split(" "))
            temp[m-1] += 1

        print("Case #{}:".format(cnt))
        for i, v in enumerate(temp):
            datetime_object = datetime.datetime.strptime(str(i+1), "%m")
            month_name = datetime_object.strftime("%b")
            print("{}:{}".format(month_name, "*"*v))




