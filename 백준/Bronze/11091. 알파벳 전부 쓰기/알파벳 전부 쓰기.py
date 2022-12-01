import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]
temp = "abcdefghijklmnopqrstuvwxyz"


for i in input_list:
    ck = ""
    a = i.lower()
    for j in temp:
        if j in a:
            pass
        else:
            ck += j

    if not ck:
        print("pangram")
    else:
        print("missing", ck)