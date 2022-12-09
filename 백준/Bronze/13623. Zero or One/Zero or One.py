import sys

abc = list(map(int, sys.stdin.readline().rstrip().split(" ")))

if abc.count(0) == 1:
    for i, v in enumerate(abc):
        if v == 0:
            print(chr(65+i))
elif abc.count(1) == 1:
    for i, v in enumerate(abc):
        if v == 1:
            print(chr(65+i))
else:
    print("*")

