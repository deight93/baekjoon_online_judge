import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    name_list = sys.stdin.readline().rstrip().split(" ")
    f_name = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    print(name_list[(name_list.index(f_name)+n)%len(name_list)-1])

