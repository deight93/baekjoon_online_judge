import sys


w = [i[0] for i in sys.stdin.readline().rstrip().split("-")]
temp = ""
for i in w:
    temp += i

print(temp)