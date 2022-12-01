
import sys

temp = []
for i in range(9):
    temp += [int(j) for j in sys.stdin.readline().rstrip().split(" ")]

print(max(temp))
print(temp.index(max(temp))//9+1, temp.index(max(temp))%9+1)