import sys

t = int(sys.stdin.readline().strip())

for c in range(t):
    n = int(sys.stdin.readline().strip())
    xi = sorted(map(int, sys.stdin.readline().strip().split(" ")))
    yi = sorted(map(int, sys.stdin.readline().strip().split(" ")), reverse=True)
    print(f'Case #{c+1}: {sum([i[0]*i[1] for i in list(zip(xi, yi))])}')
