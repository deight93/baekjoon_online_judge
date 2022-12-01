
import sys

input_list = [sys.stdin.readline().rstrip() for i in range(6)]

if input_list.count("W") in [5, 6]:
    print(1)
elif input_list.count("W") in [3, 4]:
    print(2)
elif input_list.count("W") in [1, 2]:
    print(3)
else:
    print(-1)
