import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    xy_list = [list(map(float, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]

    max_x = max(xy_list, key=lambda x: x[0])[0]
    min_x = min(xy_list, key=lambda x: x[0])[0]
    max_y = max(xy_list, key=lambda x: x[1])[1]
    min_y = min(xy_list, key=lambda x: x[1])[1]

    x = max_x+((-1)*(min_x))
    y = max_y+((-1)*(min_y))

    print("Case {}: Area {}, Perimeter {}".format(_+1, x*y, 2*(x+y)))


