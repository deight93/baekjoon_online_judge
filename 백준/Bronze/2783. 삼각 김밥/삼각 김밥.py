
import sys

x, y = map(int, sys.stdin.readline().rstrip().split(" "))
n = int(sys.stdin.readline().rstrip())
temp = [(1000/y)*x]
for _ in range(n):
    xi, yi = map(int, sys.stdin.readline().rstrip().split(" "))
    temp.append((1000 / yi) * xi)

print("{:.2f}".format(min(temp)))