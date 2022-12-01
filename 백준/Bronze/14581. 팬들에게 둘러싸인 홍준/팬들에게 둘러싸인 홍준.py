import sys

_id = sys.stdin.readline().rstrip()

emo = ":fan:"

for i in range(3):
    temp = ""
    for j in range(3):
        if i == 1:
            if j == 1:
                temp += ":{}:".format(_id)
            else:
                temp += emo
        else:
            temp += emo
    print(temp)