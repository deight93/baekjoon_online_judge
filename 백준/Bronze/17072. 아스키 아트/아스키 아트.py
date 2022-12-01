import sys


def i(r, g, b):
    return (2126*r) + (7152*g) + (722*b)


n, m = map(int, sys.stdin.readline().rstrip().split(" "))

art = []
for _ in range(n):
    t_m = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    t_m = [t_m[i:i+3] for i in range(0, len(t_m), 3)]

    art_line = ""
    for rgb in t_m:
        intensity = i(rgb[0], rgb[1], rgb[2])
        if 0 <= intensity < 510000:
            art_line += "#"
        elif 510000 <= intensity < 1020000:
            art_line += "o"
        elif 1020000 <= intensity < 1530000:
            art_line += "+"
        elif 1530000 <= intensity < 2040000:
            art_line += "-"
        else:
            art_line += "."
    art += [art_line]

for a in art:
    print(a)
