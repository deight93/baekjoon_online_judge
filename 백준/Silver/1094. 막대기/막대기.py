
import sys

x = int(sys.stdin.readline())

temp = [64]
while True:
    if sum(temp) > x:
        a = min(temp)/2
        temp.remove(min(temp))
        temp.append(a)
        if sum(temp) >= x:
            pass
        else:
            temp.append(a)
    elif sum(temp) == x:
        break
print(len(temp))