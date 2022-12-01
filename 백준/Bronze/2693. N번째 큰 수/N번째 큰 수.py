t = int(input())

list_2d = []
for i in range(t):
    temp = [int(i) for i in input().split(" ")]
    list_2d += [sorted(temp)]

for j in list_2d:
    print(j[-3])