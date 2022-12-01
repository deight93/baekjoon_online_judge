import sys

t = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline().rstrip()) for i in range(t)]

for i in input_list:
    a = [j for j in range(1, i+1) if i%j == 0]
    print(i, len(a))
