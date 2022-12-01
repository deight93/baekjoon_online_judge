
import sys

abc = map(int, sys.stdin.readline().rstrip().split(" "))

odd_list = []
even_list = []

for i in abc:
    if i % 2 != 0:
        odd_list += [i]
    else:
        even_list += [i]

temp = 1
if len(odd_list) != 0:
    for i in odd_list:
        temp *= i
else:
    for i in even_list:
        temp *= i
print(temp)
