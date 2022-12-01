import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

cnt = 0
for i in input_list:
    if k >= i:
        cnt += 1*(k//i)
        k -= i*(k//i)
print(cnt)