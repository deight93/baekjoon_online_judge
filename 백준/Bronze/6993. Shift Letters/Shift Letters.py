import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    w, n = sys.stdin.readline().rstrip().split(" ")
    l_w = list(w)
    for j in range(int(n)):
        temp = l_w.pop(-1)
        l_w.insert(0, temp)

    print("Shifting {} by {} positions gives us: {}".format(w, n, "".join(l_w)))

