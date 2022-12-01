import sys

n = int(sys.stdin.readline())
input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(n)]
print(sum([i[1]%i[0] for i in input_list]))