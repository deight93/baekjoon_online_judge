
import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

aa = a % 4
bb = b % 4
aaa = a // 4
bbb = b // 4
if aa == 0:
    aa = 4
    aaa -= 1
if bb == 0:
    bb = 4
    bbb -= 1

print(abs(bbb - aaa)+abs(aa-bb))
