import sys
from itertools import combinations

while True:
    input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if input_list[0] == 0:
        break

    for i in combinations(input_list[1:], 6):
        print(str(i).replace("(", "").replace(")", "").replace(",", ""))
    print()

