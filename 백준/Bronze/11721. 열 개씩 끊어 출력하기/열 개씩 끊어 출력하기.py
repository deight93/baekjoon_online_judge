import sys

w = sys.stdin.readline().rstrip()

for i in range(0, len(w), 10):
    print(w[i:i+10])