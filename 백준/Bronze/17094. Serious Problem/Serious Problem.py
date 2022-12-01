
import sys

s_n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

e_c = s.count("e")
two_c = s.count("2")

if e_c == two_c:
    print("yee")
elif e_c > two_c:
    print("e")
elif two_c > e_c:
    print("2")
