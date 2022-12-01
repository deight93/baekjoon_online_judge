
import sys

n = int(sys.stdin.readline().rstrip())
y = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

cnt = 0
for i in range(n):
    if y[i] == "C" and t[i] == "C":
        cnt += 1
print(cnt)

