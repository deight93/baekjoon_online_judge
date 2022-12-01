import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    input_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]

    num = sum([int(i[0]) for i in input_list])
    score = sum([int(i[0])*float(i[1]) for i in input_list])
    print(num, "{:.1f}".format(score/num))