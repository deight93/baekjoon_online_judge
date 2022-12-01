
import sys

cnt = 0
while True:
    cnt += 1
    l = int(sys.stdin.readline().rstrip())
    if l == 0:
        break
    n = int(sys.stdin.readline().rstrip())
    nn = [int(sys.stdin.readline().rstrip())*l/100000 for _ in range(n)]
    print("User {}".format(cnt))
    for i in nn:
        print("{:.5f}".format(i))

