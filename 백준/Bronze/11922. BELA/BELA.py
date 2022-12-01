import sys

card = {"A": [11, 11], "K": [4, 4], "Q": [3, 3], "J": [20, 2],
        "T": [10, 10], "9": [14, 0], "8": [0, 0], "7": [0, 0]}

n, b = sys.stdin.readline().rstrip().split(" ")

t = 0
for _ in range(4*int(n)):
    c = sys.stdin.readline().rstrip()
    if b == c[1]:
        t += card[c[0]][0]
    else:
        t += card[c[0]][1]

print(t)


