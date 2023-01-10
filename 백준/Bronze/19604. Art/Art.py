import sys

n = int(sys.stdin.readline().rstrip())
xy = [list(map(int, sys.stdin.readline().rstrip().split(","))) for _ in range(n)]
max_x = max(xy, key=lambda x: x[0])[0]
min_x = min(xy, key=lambda x: x[0])[0]
max_y = max(xy, key=lambda x: x[1])[1]
min_y = min(xy, key=lambda x: x[1])[1]

print("{},{}".format(min_x-1, min_y-1))
print("{},{}".format(max_x+1, max_y+1))


