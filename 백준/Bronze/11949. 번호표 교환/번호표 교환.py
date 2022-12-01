
import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

for i in range(1, m+1):
    for j in range(1, n):
        if input_list[j-1] % i > input_list[j] % i:
            input_list[j - 1], input_list[j] = input_list[j], input_list[j-1]

[print(i) for i in input_list]