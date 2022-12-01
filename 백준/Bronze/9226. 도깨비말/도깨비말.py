
import sys

temp = ["a", "e", "i", "o", "u"]
while True:
    n = sys.stdin.readline().rstrip()
    if n == "#":
        break

    if len(set(temp)-set(n)) == 5 or n[0] in temp:
        n += "ay"
    else:
        while True:
            if n[0] in temp:
                n += "ay"
                break
            else:
                a = n[0]
                b = n[1:]
                n = b+a
    print(n)