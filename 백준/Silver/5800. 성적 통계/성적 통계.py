import sys

t = int(sys.stdin.readline())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for i in range(t)]
temp = []
for i in input_list:
    v = sorted(i[1:])
    temp += [(max(v), min(v), max([v[j]-v[j-1] for j in range(1, len(v))]))]

for k, v in enumerate(temp):
    print("Class {}".format(k+1))
    print("Max {}, Min {}, Largest gap {}".format(v[0], v[1], v[2]))