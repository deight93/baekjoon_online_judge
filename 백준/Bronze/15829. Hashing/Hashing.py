import sys

l = int(sys.stdin.readline().rstrip())
w = sys.stdin.readline().rstrip()

r = 0
for i, v in enumerate(w):
    r += ((31**i)*(ord(v)-96))

print(r % 1234567891)

