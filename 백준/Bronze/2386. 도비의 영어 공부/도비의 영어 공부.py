import sys

while True:
    n = [i for i in sys.stdin.readline().rstrip().split(" ")]
    if n[0] == "#":
        break

    temp = ""
    for i in n[1:]:
        temp += i
    print(n[0], temp.lower().count(n[0]))