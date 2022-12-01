import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    k = sys.stdin.readline().rstrip().split()
    even = []
    odd = []
    for j in k[1:]:
        if int(j)%2 == 0:
            even.append(int(j))
        else:
            odd.append(int(j))
    if sum(even) > sum(odd):
        print("EVEN")
    elif sum(even) < sum(odd):
        print("ODD")
    else:
        print('TIE')


