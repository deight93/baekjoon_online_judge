import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    s = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
    s_ck = s[1] - s[2]
    temp = s[2]
    ck = 0
    for j in s[3:]:
        if s_ck != temp-j:
            ck = 1
            break
        else:
            temp = j

    if ck == 0:
        print("The next 5 numbers after {} are: {}".format(str(s[1:]), str([s[-1]+(-1*(s_ck)*i) for i in range(1, 6)])))
    else:
        print("The sequence {} is not an arithmetic sequence.".format(str(s[1:])))

