import sys


temp_dict = {"%": "%25", " ": "%20", "!": "%21", "$": "%24", "(": "%28", ")": "%29", "*": "%2a"}

while True:
    n = sys.stdin.readline().rstrip()
    if n == '#':
        break
    else:
        for i in temp_dict.keys():
            if n.find(i) != -1:
                n = n.replace(i, temp_dict[i])
        print(n)
