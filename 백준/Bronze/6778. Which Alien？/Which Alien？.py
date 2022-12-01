
import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())

if a >= 3 and b <= 4:
    print("TroyMartian")

if a <= 6 and b >= 2:
    print("VladSaturnian")

if a <= 2 and b <= 3:
    print("GraemeMercurian")


