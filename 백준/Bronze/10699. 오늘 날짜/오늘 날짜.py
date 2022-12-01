import datetime


KST = datetime.timezone(datetime.timedelta(hours=9))
from1 = datetime.datetime.strftime(datetime.datetime.now(tz=KST), "%Y-%m-%d")
print(from1)