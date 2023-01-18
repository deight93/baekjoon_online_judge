import sys

n, h, w = map(int, sys.stdin.readline().rstrip().split(" "))
init_s = ["?"]*n

for _ in range(h):
    s = sys.stdin.readline().rstrip()
    for i in range(n):
        s_s = s[i*w:(i*w)+w]
        set_ss = list(set(s_s))
        if set_ss != ["?"]:
            if "?" in set_ss:
                set_ss.remove("?")
            if init_s[i] == "?":
                init_s[i] = set_ss[0]

print("".join(init_s))