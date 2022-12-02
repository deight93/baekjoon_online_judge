import sys
species = {"B": ["Bobcat", 2], "C": ["Coyote", 1], "M": ["Mountain Lion", 4], "W": ["Wolf", 3]}

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    fw, sw = sys.stdin.readline().rstrip().split(" ")
    ck_dict = {}
    for i in sw:
        if species[i][0] in ck_dict:
            ck_dict[species[i][0]] += species[i][1]
        else:
            ck_dict[species[i][0]] = species[i][1]

    if list(ck_dict.values()).count(max(ck_dict.values())) == 1:
        m = max(ck_dict.items(), key=lambda x: x[1])
        print("{}: The {} is the dominant species".format(fw, m[0]))
    else:
        print("{}: There is no dominant species".format(fw))
