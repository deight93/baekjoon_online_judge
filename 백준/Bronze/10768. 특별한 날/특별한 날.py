import sys
import datetime

input_list = [sys.stdin.readline().rstrip() for _ in range(2)]
a = datetime.datetime(year=2015, month=int(input_list[0]), day=int(input_list[1]))

if datetime.datetime.strptime("2015-02-18", "%Y-%m-%d") > a:
    print("Before")
elif datetime.datetime.strptime("2015-02-18", "%Y-%m-%d") < a:
    print("After")
else:
    print("Special")