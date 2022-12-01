import sys

n = int(sys.stdin.readline())

temp_list = []
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for i in range(n):
    input_list = [int(i) for i in sys.stdin.readline().split()]
    x = input_list[0]
    y = input_list[1]

    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print("""Q1: {}
Q2: {}
Q3: {}
Q4: {}
AXIS: {}""".format(q1, q2, q3, q4, axis))