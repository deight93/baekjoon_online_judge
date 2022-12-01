import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == "0":
        break

    n = n.split(" ")[1:]
    temp = [n[0]]
    for i in range(1, len(n)):
        if n[i-1] != n[i]:
            temp += [n[i]]

    print(" ".join(temp)+" $")