import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    for i in range(m, 0, -1):
        str_i = str(i)
        if i == int("".join(sorted(str(i)))):
            print("Case #{}: {}".format(_+1, i))
            break
