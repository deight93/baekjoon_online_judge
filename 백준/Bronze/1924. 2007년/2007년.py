import sys
import datetime

input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
temp = "MON, TUE, WED, THU, FRI, SAT, SUN".split(", ")
print(temp[datetime.datetime(year=2007, month=input_list[0], day=input_list[1]).weekday()])