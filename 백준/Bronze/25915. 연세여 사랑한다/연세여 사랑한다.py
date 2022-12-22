import sys

c = sys.stdin.readline().rstrip()
temp = [ord(i) for i in "ILOVEYONSEI"]
t = 0
for i in range(1, len(temp)):
    t += abs(temp[i-1]-temp[i])
print(t + abs(ord(c)-temp[0]))

