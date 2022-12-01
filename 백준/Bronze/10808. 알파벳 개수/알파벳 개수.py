import sys

w = sys.stdin.readline().rstrip()
temp = {}
a = [chr(i) for i in range(ord("a"), ord("z")+1)]
for i in a:
    temp[i] = 0

for i in w:
    temp[i]+=1

[print(_, end=" ") for _ in temp.values()]