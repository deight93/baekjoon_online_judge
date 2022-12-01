import sys

c = int(input())
for i in range(1, c+1):
    input_list = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    print("Case #{}: {}".format(i, input_list[0]+input_list[1]))
