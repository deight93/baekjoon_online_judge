import sys

g = [1, 2, 3, 3, 4, 10]
s = [1, 2, 2, 2, 3, 5, 10]

n = int(sys.stdin.readline())
input_list = [[list(map(int, sys.stdin.readline().rstrip().split(" "))), list(map(int, sys.stdin.readline().rstrip().split(" ")))] for _ in range(n)]

for k, i in enumerate(input_list):
    g_s = sum([x * y for x, y in zip(i[0], g)])
    s_s = sum([x * y for x, y in zip(i[1], s)])
    if g_s > s_s:
        temp = "Good triumphs over Evil"
    elif g_s < s_s:
        temp = "Evil eradicates all trace of Good"
    else:
        temp = "No victor on this battle field"
    print("Battle {}: {}".format(k+1, temp))
