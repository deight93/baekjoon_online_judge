
import sys

temp = {
"-": 0,
"!": 1, # \ -> !
"(": 2,
"@": 3,
"?": 4,
">": 5,
"&": 6,
"%": 7,
"/": -1
}

while True:
    octopus = sys.stdin.readline().rstrip()
    if octopus == "#":
        break

    octopus = octopus.replace("\\", "!")
    total = 0
    for k, i in enumerate(octopus):
        e = len(octopus)-k-1
        v = temp[i]*8**e
        total += v
    print(total)