import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip().lower()
    if 'pink' in s or 'rose' in s:
        cnt += 1

if not cnt:
    print('I must watch Star Wars with my daughter')
else:
    print(cnt)
