import sys

n = int(sys.stdin.readline().rstrip())
init_x, init_y = map(int, sys.stdin.readline().rstrip().split(" "))
temp_x, temp_y = init_x, init_y

t = 0
for i in range(n-1):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    t = t + ((temp_x-x)**2 + (temp_y-y)**2)**0.5
    temp_x, temp_y = x, y
t = t + ((init_x-x)**2 + (init_y-y)**2)**0.5
print(int(t))

