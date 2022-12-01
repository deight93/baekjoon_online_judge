import sys

snu = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(3)]
print(max(list(zip(["S", "N", "U"], [i[1]*10/((i[0]*10)-500 if i[0]*10 >= 5000 else i[0]*10) for i in snu])), key=lambda x: x[1])[0])



