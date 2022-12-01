import sys
import datetime

d, h, m = map(int, sys.stdin.readline().strip().split(" "))
td = datetime.datetime(2011,11,d,h,m) - datetime.datetime(2011,11,11,11,11)
tdm = int(td.total_seconds()/60)

if tdm < 0:
    print(-1)
else:
    print(tdm)
