import sys

n = int(sys.stdin.readline().rstrip())
input_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

if max(input_list) == input_list[0]:
    print("S")
else:
    print("N")