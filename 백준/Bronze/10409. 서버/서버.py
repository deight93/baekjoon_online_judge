import sys

n, t = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]

cnt = 0
for i in input_list:
    t -= i
    if t >= 0:
        cnt += 1
print(cnt)