import sys

temp = {"1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"}

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
temp2 = []
for i in range(n, m+1):
    temp2 += [(i, " ".join([temp[j] for j in str(i)]))]

r = sorted(temp2, key=lambda x: x[1])
for i in range(len(r)//10+1):
    print(" ".join([str(i[0]) for i in r[i*10:(i+1)*10]]))