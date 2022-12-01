
import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = sys.stdin.readline().rstrip()

    if len(n) == 8:
        if n[0].isnumeric() and int(n[0]) in range(1, 10) and n[0] == n[1]:
            if all([True if n[i].isnumeric() and int(n[i]) in range(1, 10) else False for i in range(2, 4)]):
                if n[4].isalpha() and n[4].isupper():
                    if all([True if n[i].isnumeric() and int(n[i]) in range(1, 10) else False for i in range(5, 8)]):
                        print(n)


