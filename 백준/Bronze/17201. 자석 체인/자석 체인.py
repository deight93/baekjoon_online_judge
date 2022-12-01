
import sys

n = int(sys.stdin.readline().rstrip())
a = sys.stdin.readline().rstrip()

if a.find("11") != -1 or a.find("22") != -1:
    print("No")
else:
    print("Yes")

