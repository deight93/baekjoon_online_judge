import sys

n = int(sys.stdin.readline().rstrip())

set_list = [0, 0, 0]
for _ in range(n):
    abc = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    set_list = [sum(i) for i in list(zip(set_list, abc))]
    if min(set_list) < 30:
        print("NO")
    else:
        print(min(set_list))
        set_list = [i-min(set_list) for i in set_list]

