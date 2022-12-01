import sys

d = [int(sys.stdin.readline().rstrip()) for i in range(4)]

if d[0] < d[1] < d[2] < d[3]:
    print("Fish Rising")
elif d[0] > d[1] > d[2] > d[3]:
    print("Fish Diving")
elif d[0] == d[1] == d[2] == d[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")
