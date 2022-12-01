import sys

n = int(sys.stdin.readline())
input_list = [[int(i) for i in sys.stdin.readline().rstrip().split(" ")] for _ in range(n)]

for i in input_list:
    print("You get {} piece(s) and your dad gets {} piece(s).".format(i[0]//i[1], i[0]%i[1]))