import sys

temp = {0: "1QAZ",
        1: "2WSX",
        2: "3EDC",
        3: "45RFVTGB",
        4: "67YHNUJM",
        5: "8IK,",
        6: "9OL.",
        7: "0-=P[];\'/"}

a = sys.stdin.readline().rstrip()
r = [0 for _ in range(8)]

for i in a:
    for k, v in temp.items():
        if v.count(i) != 0:
            r[k] += 1

for i in r:
    print(i)

