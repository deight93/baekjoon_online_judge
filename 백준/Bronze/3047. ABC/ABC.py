import sys
num_list = sorted([int(i) for i in sys.stdin.readline().rstrip().split(" ")])
order = sys.stdin.readline().rstrip()

num_dict = {"A": num_list[0],
            "B": num_list[1],
            "C": num_list[2]}

for j in order:
    print(num_dict[j], end=" ")