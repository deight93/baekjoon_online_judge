import sys

n = int(sys.stdin.readline().rstrip())
temp1 = [chr(i) for i in range(65, 91)]
temp2 = {}
for i in range(int(len(temp1)//2)):
    temp2[temp1[i]] = temp1[int(len(temp1)-i)-1]
    temp2[temp1[int(len(temp1)-i)-1]] = temp1[i]

for i in range(n):
    t = sys.stdin.readline().rstrip().upper()
    ck = 0
    if len(t)%2 != 0:
        ck = 1

    for j in t:
        if j.isalnum():
            if temp2[j] not in t:
                ck = 1
        else:
            pass

    if ck == 1:
        print("No")
    else:
        print("Yes")
