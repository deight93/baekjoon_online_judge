
import sys

temp = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3),
        'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3),
        'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3),
        'M': (3, 0), 'N': (3, 1), 'O': (3, 2), '.': (3, 3)}

t_list = [sys.stdin.readline().rstrip() for _ in range(4)]

t = 0
for k, i in enumerate(t_list):
    for k2, j in enumerate(i):
        if j != ".":
            t += abs(k-temp[j][0])+abs(k2-temp[j][1])

print(t)

