import sys

case = 0
while True:
    s = sys.stdin.readline().rstrip().split(" ")
    s1 = int(s[0])
    s2 = int(s[2])

    case += 1
    if s[1] == "E":
        break
    else:
        if ">" == s[1]:
            temp = s1 > s2
        elif ">=" == s[1]:
            temp = s1 >= s2
        elif "<" == s[1]:
            temp = s1 < s2
        elif "<=" == s[1]:
            temp = s1 <= s2
        elif "==" == s[1]:
            temp = s1 == s2
        elif "!=" == s[1]:
            temp = s1 != s2

        print("Case {}: {}".format(case, str(temp).lower()))