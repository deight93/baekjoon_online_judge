
import sys

w_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(10)])
k_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(10)])

print(sum(w_list[-3:]), sum(k_list[-3:]))