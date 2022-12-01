
import sys

temp = [0]
for i in range(1, 45):
    temp.append(temp[i-1] + i)
temp = temp[1:]
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    total = []
    for i in range(len(temp)):
        for j in range(i, len(temp)):
            for k in range(j, len(temp)):
                if n == temp[i]+temp[j]+temp[k]:
                    total += [n]
                    break

    print(len(set(total)))
