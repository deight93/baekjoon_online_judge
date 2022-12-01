import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    i_l = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    hp = i_l[0] + i_l[4]
    mp = i_l[1] + i_l[5]
    a = i_l[2] + i_l[6]
    s = i_l[3] + i_l[7]

    if hp < 1: hp = 1
    if mp < 1: mp = 1
    if a < 0: a = 0

    combat = 1 * hp + 5 * mp + 2 * a + 2 * s
    print(combat)