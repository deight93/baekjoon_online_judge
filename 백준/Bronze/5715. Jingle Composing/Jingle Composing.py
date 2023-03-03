import sys

note = {"W": 1,
        "H": 1/2,
        "Q": 1/4,
        "E": 1/8,
        "S": 1/16,
        "T": 1/32,
        "X": 1/64}

while True:
    s = sys.stdin.readline().rstrip()
    if s == "*":
        break
    else:
        s_list = s[1:-1].split("/")
        cnt = 0
        for i in s_list:
            duration = 0
            for j in i:
                duration += note[j]

            if duration == 1:
                cnt += 1
        print(cnt)