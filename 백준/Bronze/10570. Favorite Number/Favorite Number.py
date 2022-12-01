import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    v = int(sys.stdin.readline().rstrip())

    s_dict = {}
    for i in range(v):
        s = int(sys.stdin.readline().rstrip())
        if s in s_dict.keys():
            s_dict[s] += 1
        else:
            s_dict[s] = 1
    print(max(sorted(s_dict.items()), key=lambda x: x[1])[0])