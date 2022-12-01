import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

r = {'.': '.', 'O': 'O', '-': '|', '|': '-', '/': '\\', '\\': '/', '^': '<', '<': 'v',
     'v': '>', '>': '^'}

milk = [sys.stdin.readline().rstrip() for _ in range(n)]
t_milk = list(zip(*milk))

for idx1, i in enumerate(t_milk):
    t_milk[idx1] = list(i)
    for idx2, j in enumerate(t_milk[idx1]):
        t_milk[idx1][idx2] = r[j]

for i in t_milk[::-1]:
    print("".join(i))

