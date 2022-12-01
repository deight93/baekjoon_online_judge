
import sys

temp = [["1", "2"], ["3", "4"]]

n = sys.stdin.readline().rstrip()

for i in n:
    if i == "H":
        temp.reverse()
    else:
        temp[0].reverse()
        temp[1].reverse()

for i in temp:
    print(" ".join(i))
