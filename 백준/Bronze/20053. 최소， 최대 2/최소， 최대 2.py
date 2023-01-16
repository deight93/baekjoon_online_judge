import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    integers = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    print(min(integers), max(integers))