import sys

n = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
temp = [((i-1) % 5)+1 for i in range(1, 11)]

for k, i in enumerate(input_list):
    if i == temp:
        print(k+1)