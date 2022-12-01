
import sys

while True:
    n = sys.stdin.readline().rstrip()
    if n == "#":
        break
    a_list = [i.lower() for i in n if i.isalpha() is True]
    print(len(set(a_list)))
