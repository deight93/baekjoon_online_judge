
import sys

p_ab, p_bc, p_cd = map(int, sys.stdin.readline().rstrip().split(" "))


if p_ab == p_bc == p_cd:
    p_ad = p_bc
else:
    p_ad = (p_ab*p_cd)/p_bc

print(p_ad)


