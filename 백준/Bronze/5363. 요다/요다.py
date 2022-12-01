import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

for i in input_list:
    print(" ".join(i[2:]+i[:2]))