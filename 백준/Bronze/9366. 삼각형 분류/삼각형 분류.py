import sys

t = int(sys.stdin.readline().rstrip())
input_list = [[int(j) for j in sys.stdin.readline().rstrip().split(" ")] for _ in range(t)]

for k, i in enumerate(input_list):
    set_i = set(i)
    max_i = max(i)
    i.remove(max_i)
    if max_i < sum(i):
        if len(set_i) == 1:
            temp = "equilateral"
        elif len(set_i) == 2:
            temp = "isosceles"
        else:
            temp = "scalene"
    else:
        temp = "invalid!"
    print("Case #{}: {}".format(k + 1, temp))
