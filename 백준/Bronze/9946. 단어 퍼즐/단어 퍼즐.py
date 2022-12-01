import sys

cnt = 0
while True:
    cnt += 1
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    if a == "END" and b == "END":
        break

    if sorted(a) == sorted(b):
        print("Case {}: same".format(cnt))
    else:
        print("Case {}: different".format(cnt))