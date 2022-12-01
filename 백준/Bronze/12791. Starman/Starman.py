import sys

t = int(sys.stdin.readline().rstrip())
temp = """1967 DavidBowie,
1969 SpaceOddity,
1970 TheManWhoSoldTheWorld,
1971 HunkyDory,
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars,
1973 AladdinSane,
1973 PinUps,
1974 DiamondDogs,
1975 YoungAmericans,
1976 StationToStation,
1977 Low,
1977 Heroes,
1979 Lodger,
1980 ScaryMonstersAndSuperCreeps,
1983 LetsDance,
1984 Tonight,
1987 NeverLetMeDown,
1993 BlackTieWhiteNoise,
1995 1.Outside,
1997 Earthling,
1999 Hours,
2002 Heathen,
2003 Reality,
2013 TheNextDay,
2016 BlackStar""".split(",")
temp = [i.strip().split(" ") for i in temp]

temp_dict = {}
for i in temp:
    if int(i[0]) in temp_dict.keys():
        temp_dict[int(i[0])] += [i[1]]
    else:
        temp_dict[int(i[0])] = [i[1]]

for _ in range(t):
    s, e = map(int, sys.stdin.readline().rstrip().split(" "))

    cnt = 0
    for i in range(s, e+1):
        if i in temp_dict.keys():
            cnt += len(temp_dict[i])
    print(cnt)

    for i in range(s, e+1):
        if i in temp_dict.keys():
            for j in temp_dict[i]:
                print("{} {}".format(i, j))