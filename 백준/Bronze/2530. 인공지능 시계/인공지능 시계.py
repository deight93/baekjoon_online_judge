import sys
import datetime

input_list = [int(i) for i in sys.stdin.readline().split(" ")]
p_s = int(sys.stdin.readline().rstrip())
h = input_list[0]
m = input_list[1]
s = input_list[2]

temp = datetime.datetime(year=1, month=1, day=1, hour=h, minute=m, second=s) + datetime.timedelta(seconds=p_s)
print(temp.time().hour, temp.time().minute, temp.time().second)