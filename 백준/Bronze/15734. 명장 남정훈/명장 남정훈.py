import sys

l, r, a = map(int, sys.stdin.readline().rstrip().split(" "))
l_r = sorted([l, r])

if len(set(l_r)) == 1:
    print(l+r+((a//2)*2))
else:
    if l_r[1]-l_r[0] <= a:
        temp = l_r[1]-l_r[0]
        print(l_r[0]+l_r[1]+temp+(((a-temp)//2)*2))
    else:
        print(2*(l_r[0]+a))