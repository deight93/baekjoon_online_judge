import sys

n = int(sys.stdin.readline().rstrip())
s_c = 0
t_c = 0

for _ in range(n):
    t = sys.stdin.readline().rstrip()
    s_c += t.count("s")
    s_c += t.count("S")
    t_c += t.count("t")
    t_c += t.count("T")

if s_c >= t_c:
    print("French")
else:
    print("English")

