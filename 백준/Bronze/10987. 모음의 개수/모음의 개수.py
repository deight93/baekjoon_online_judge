import sys

w = sys.stdin.readline().rstrip()
temp = ["a", "e", "i", "o", "u"]

c = 0
for i in temp:
    c += w.count(i)
print(c)