
import sys

temp = {"A+": list(range(97, 101)),
        "A": list(range(90, 97)),
        "B+": list(range(87, 90)),
        "B": list(range(80, 87)),
        "C+": list(range(77, 80)),
        "C": list(range(70, 77)),
        "D+": list(range(67, 70)),
        "D": list(range(60, 67)),
        "F": list(range(0, 60))}

for _ in range(int(sys.stdin.readline().rstrip())):
    input_list = sys.stdin.readline().rstrip().split(" ")
    n = input_list[0]
    s = int(input_list[1])

    for k, v in temp.items():
        if s in v:
            print(n, k)