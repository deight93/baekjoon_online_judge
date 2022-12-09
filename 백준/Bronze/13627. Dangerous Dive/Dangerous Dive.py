import sys

n, r = map(int, sys.stdin.readline().rstrip().split(" "))
v_n = set([i for i in range(1, n+1)])
i_r = set(list(map(int, sys.stdin.readline().rstrip().split(" "))))
r_m = v_n - i_r

if r_m:
    print(" ".join(list(map(str, sorted(r_m))))+" ")
else:
    print("*")


