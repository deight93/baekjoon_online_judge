import sys

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline().rstrip() for _ in range(n)]

for k, i in enumerate(input_list):
    temp = ""
    for j in i:
        if j == "Z":
            temp += "A"
        else:
            temp += chr(ord(j)+1)
    print("String #{}".format(k+1))
    print(temp)
    if len(input_list)-1 != k:
        print()
