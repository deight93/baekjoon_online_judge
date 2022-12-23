import sys

n = int(sys.stdin.readline().rstrip())
ab = [tuple(sys.stdin.readline().rstrip().split(" ")) for _ in range(n)]
ab = sorted(ab, key=lambda x: x[1], reverse=True)
ab = sorted(ab, key=lambda x: x[0])
for i in ab:
    print(" ".join(i))

