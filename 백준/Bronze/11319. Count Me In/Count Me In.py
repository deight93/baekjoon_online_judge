
import sys

v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip().replace(" ", "")

    v_t = 0
    c_t = 0
    for i in s:
        if i in v:
            v_t += 1
        else:
            c_t += 1
    print(c_t, v_t)

