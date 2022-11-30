
import sys

a, b = sys.stdin.readline().rstrip().split(" ")

len_ab = len(b)-len(a)
temp = []
for i in range(len_ab+1):
    t = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            t += 1
    temp.append(t)
print(min(temp))
