
import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    t_list = [sys.stdin.readline().rstrip().split(" ") for _ in range(n)]
    t = max(t_list, key=lambda x: float(x[1]))

    r_list = [i[0] for i in t_list if i[1] == t[1]]
    print(" ".join(r_list))

