
import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    avg_n = sum(n_list)/n

    cnt = sum([1 if i <= avg_n else 0 for i in n_list])
    print(cnt)
