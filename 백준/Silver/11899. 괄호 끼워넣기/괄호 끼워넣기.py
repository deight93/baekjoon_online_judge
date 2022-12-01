
import sys

n = sys.stdin.readline().rstrip()

while True:
    if n.find("()") != -1:
        n = n.replace("()", "")
    else:
        break

print(len(n))