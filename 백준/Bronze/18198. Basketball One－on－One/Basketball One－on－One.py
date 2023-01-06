import sys

c = sys.stdin.readline().rstrip()
temp = {"A": 0, "B": 0}

for i in range(0, len(c), 2):
    temp[c[i:i+2][0]] += int(c[i:i+2][1])

print(max(temp.items(), key=lambda x: x[1])[0])

