
import sys
import datetime

input_list = [datetime.datetime.strptime(sys.stdin.readline().rstrip(), "%H:%M:%S") for _ in range(2)]
if str(input_list[0].time()) == str(input_list[1].time()):
    print('24:00:00')
else:
    print((input_list[1] - datetime.timedelta(hours=input_list[0].hour, minutes=input_list[0].minute,
                                              seconds=input_list[0].second)).time())