import sys

n = int(sys.stdin.readline())

for i in range(n):
    n2 = int(sys.stdin.readline())
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    print((max(input_list)-min(input_list))*2)