import sys
import datetime

input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(3)]

for i in input_list:
    a = datetime.datetime(year=2020, month=1, day=1, hour=i[3], minute=i[4],
                          second=i[5]) - datetime.timedelta(hours=i[0], minutes=i[1], seconds=i[2])
    print(a.hour, a.minute, a.second)