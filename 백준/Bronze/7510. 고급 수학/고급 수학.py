import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_list = sorted([int(i) for i in sys.stdin.readline().rstrip().split(" ")])

    a = input_list[0]
    b = input_list[1]
    c = input_list[2]
    if (a**2+b**2)**0.5 == c:
        print("Scenario #{}:".format(i + 1))
        print("yes\n")
    else:
        print("Scenario #{}:".format(i + 1))
        print("no\n")