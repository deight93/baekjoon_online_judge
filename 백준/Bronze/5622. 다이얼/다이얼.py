temp_list = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
             ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

c = input()


s = 2
total = 0
for i in temp_list:
    s += 1
    for j in c:
        for k in i:
            if ord(j) == ord(k):
                total += s

print(total)