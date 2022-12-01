import sys
import datetime

input_list = [int(i) for i in sys.stdin.readline().split(" ")]
p_m = int(sys.stdin.readline().rstrip())
h = input_list[0]
m = input_list[1]

temp = datetime.datetime(year=1, month=1, day=1, hour=h, minute=m) + datetime.timedelta(minutes=p_m)
print(temp.time().hour, temp.time().minute)