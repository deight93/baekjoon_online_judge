
import sys

input_list = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

t = 0
temp = []
for i in input_list:
    t += i
    temp.append((abs(t - 100), -1*t))
print(-1*min(temp, key=lambda x: (x[0], x[1]))[1])
