import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

if 60+k >= n:
    print(n*1500)
else:
    print(((n-(60+k))*3000)+((60+k)*1500))

