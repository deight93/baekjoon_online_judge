import sys

f_s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    a = sys.stdin.readline().rstrip()

    if a.find(f_s) == -1:
        for i in range(1, len(f_s)):
            temp = a[i:]+a[:i]
            if temp.find(f_s) != -1:
                cnt += 1
                break
    else:
        cnt += 1

print(cnt)