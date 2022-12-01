
import sys

p1, s1 = map(int, sys.stdin.readline().rstrip().split(" "))  # p_home
s2, p2 = map(int, sys.stdin.readline().rstrip().split(" "))  # s_home

if p1 + p2 > s1 + s2:
    print("Persepolis")
elif p1 + p2 < s1 + s2:
    print("Esteghlal")
else:
    if s1 < p2:
        print("Persepolis")
    elif s1 > p2:
        print("Esteghlal")
    else:
        print("Penalty")

