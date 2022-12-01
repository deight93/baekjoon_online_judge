import sys
import datetime

input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
temp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(temp[datetime.datetime(year=2009, month=input_list[1], day=input_list[0]).weekday()])