import sys

a, b = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
if a-((a/100)*b) >= 100:
    print(0)
else:
    print(1)
