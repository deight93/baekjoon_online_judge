import sys

n = int(sys.stdin.readline().rstrip())

temp = []
for i in ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']:
    a = max(map(int, sys.stdin.readline().rstrip().split(" ")))
    temp += [(i, a)]
print(max(temp, key=lambda x: x[1])[0])

