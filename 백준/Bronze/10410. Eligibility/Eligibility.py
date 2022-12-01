import sys
import datetime

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    name, psd, bd, c = sys.stdin.readline().strip().split(" ")
    psd_date = datetime.date(*list(map(int, psd.split("/"))))
    bd_date = datetime.date(*list(map(int, bd.split("/"))))

    if psd_date >= datetime.date(2010, 1, 1) or bd_date >= datetime.date(1991, 1, 1):
        print(name, "eligible")
    else:
        if int(c) >= 41:
            print(name, "ineligible")
        else:
            print(name, "coach petitions")


