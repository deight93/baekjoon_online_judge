import sys

n = int(sys.stdin.readline().rstrip())
num = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
c_num = [i for i in range(1, num[-1]+1)]
r = set(c_num)-set(num)

if r:
    for i in sorted(r):
        print(i)
else:
    print("good job")

