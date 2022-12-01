import sys

p, q, s = map(int, sys.stdin.readline().rstrip().split(" "))

p_list = set()
for i in range(1, (s//p)+1):
    p_list.add(i*p)

q_list = set()
for i in range(1, (s//q)+1):
    q_list.add(i*q)

intersection = q_list & p_list
if len(intersection) != 0:
    print("yes")
else:
    print("no")


