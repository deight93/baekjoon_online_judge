import sys
import datetime

m = sys.stdin.readline().rstrip()
n = sys.stdin.readline().rstrip()

a = datetime.datetime(2008, 3, 3, int(n[:2]), int(n[3:5]), int(n[6:])) - datetime.timedelta(hours=int(m[:2]), minutes=int(m[3:5]), seconds=int(m[6:]))

print(a.time())