import sys
import datetime

input_list = [sys.stdin.readline().rstrip() for i in range(2)]
b_day = datetime.datetime.strptime(input_list[0], "%Y %m %d")
r_day = datetime.datetime.strptime(input_list[1], "%Y %m %d")

if b_day.year == r_day.year:
    print(0)
else:
    if b_day.month > r_day.month:
        print(r_day.year - b_day.year - 1)

    elif b_day.month == r_day.month:
        if b_day.day > r_day.day:
            print(r_day.year - b_day.year - 1)
        elif b_day.day <= r_day.day:
            print(r_day.year - b_day.year)

    elif b_day.month < r_day.month:
        print(r_day.year - b_day.year)

print(r_day.year - b_day.year+1)
print(r_day.year - b_day.year)