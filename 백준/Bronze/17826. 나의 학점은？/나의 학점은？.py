import sys

s = map(int, sys.stdin.readline().rstrip().split(" "))
hs = int(sys.stdin.readline().rstrip())
ihs = list(s).index(hs)

if 0 <= ihs <= 4:
    print("A+")
elif 5 <= ihs <= 14:
    print("A0")
elif 15 <= ihs <= 29:
    print("B+")
elif 30 <= ihs <= 34:
    print("B0")
elif 35 <= ihs <= 44:
    print("C+")
elif 45 <= ihs <= 47:
    print("C0")
else:
    print("F")

