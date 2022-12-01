import sys

t = int(sys.stdin.readline().rstrip())
temp = [[9.23076, 26.7, 1.835], [1.84523, 75, 1.348], [56.0211, 1.5, 1.05], [4.99087, 42.5, 1.81],
        [0.188807, 210, 1.41], [15.9803, 3.8, 1.04], [0.11193, 254, 1.88]]

for _ in range(t):
    input_list = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]

    total = 0
    for k, p in enumerate(input_list):
        a = temp[k][0]
        b = temp[k][1]
        c = temp[k][2]

        if k % 3 == 0:
            total += int(a * ((b-p) ** c))
        else:
            total += int(a * ((p-b) ** c))

    print(total)