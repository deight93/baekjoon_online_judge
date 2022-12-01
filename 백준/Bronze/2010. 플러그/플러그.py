import sys

n = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip())-1 for _ in range(n)]
input_list.append(1)
print(sum(input_list))