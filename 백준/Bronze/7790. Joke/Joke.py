
import sys

a = sys.stdin.readlines()
cnt = 0
for i in a:
    cnt += i.count("joke")

print(cnt)
